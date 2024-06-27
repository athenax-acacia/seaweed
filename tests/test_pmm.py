# Testing for PMM class

# Import packages
import pytest
import warnings
import types
import numpy as np
import qmcpy as qp
import gc
from dataclasses import dataclass
from pathlib import Path
import subprocess

from seaweed import post_manoeuvre

# Skip all these tests if sage isn't installed in the environment
sage = pytest.importorskip('sage', reason="Sage is not installed")
warnings.filterwarnings("ignore")
from sage.all import *

# Set wd
project_root = Path(__file__).parents[1]
sagedir = project_root/'sage'
load_attach_path(str(sagedir))
sage.repl.load.load('pmm.sage', globals())


# Create all derivatives up to order 4
orders1 = get_Nth_orders(1)
orders2 = get_Nth_orders(2)
orders3 = get_Nth_orders(3)
orders4 = get_Nth_orders(4)

@dataclass(frozen=True)
class Cartesian:
    x: float
    y: float
    vx: float
    vy: float

    def __post_init__(self) -> None:
        super().__setattr__('x', float(self.x))
        super().__setattr__('y', float(self.y))
        super().__setattr__('vx', float(self.vx))
        super().__setattr__('vy', float(self.vy))

@dataclass(frozen=True)
class LPC:
    beta: float
    beta_dot: float
    rho_dot: float
    rho: float

    @classmethod
    def make(cls, relative_state: Cartesian):
        r = np.sqrt((relative_state.x)**2 + (relative_state.y)**2)
        beta = np.arctan2(relative_state.x, relative_state.y)
        beta_dot = ((relative_state.vx) * np.cos(beta) - (relative_state.vy) * np.sin(beta)) / r
        rho_dot = ((relative_state.vx) * np.sin(beta) + (relative_state.vy) * np.cos(beta)) / r
        return LPC(beta=beta, beta_dot=beta_dot, rho_dot=rho_dot, rho=np.log(r))

@dataclass(frozen=True)
class PythonEstimable:
    deltas: list
    x: list | LPC
    orders: list

def make_lpc_for_test(x, y, vx, vy):
    """ Create subscriptable list of LPC coordinates for testing

    Parameters
    ----------
    x: float
        Cartesian position in x
    y: float
        Cartesian position in y
    vx: float
        Cartesian velocity in x
    vy: float
        Cartesian velocity in y

    Return
    ------
    lpc_coords: list
        LPC coordinates in subscriptable form
    """

    # Create Cartesian object
    cartesian_coords = Cartesian(x=x, y=y, vx=vx, vy=vy)

    # Convert
    lpc_coords = LPC.make(relative_state=cartesian_coords)

    # Write out as an array
    return np.array([lpc_coords.beta, lpc_coords.beta_dot, lpc_coords.rho_dot, lpc_coords.rho])


# Create some tests
def pmm_python_estimable(orders):
    fcn_name = f'pmm_python_estimable_{orders[0]}_{orders[1]}_{orders[2]}_{orders[3]}'
    fcn_code = compile(source=f'''def {fcn_name}(delta_v, x, orders)''' + ''':
    # Define components of state space
    beta = x[0]
    rho = x[3]
    r = np.exp(rho)

    # Repeat variables according to orders
    x = np.repeat(x, orders)

    # Define coefficients and repeat according to orders
    a = np.repeat([0, delta_v[1], -delta_v[0], 0], orders)
    b = np.repeat([0, -delta_v[0], -delta_v[1], 0], orders)

    return np.prod(x + a * np.sin(beta) / r + b * np.cos(beta) / r)
    ''', filename="fcn_name", mode='exec')

    return types.FunctionType(fcn_code.co_consts[0], globals(), fcn_name)


coordinate_list = [make_lpc_for_test(0, 150000, 10, -5) for _ in range(5)]
coordinate_list[1][0] = coordinate_list[1][0] + 10
coordinate_list[2][0] = coordinate_list[2][0] - 10
coordinate_list[3][0] = coordinate_list[3][0] + 170
coordinate_list[4][0] = coordinate_list[4][0] - 170

deltas = [5, -6]
estimable_inputs = [PythonEstimable(deltas, cl, orders) for cl in coordinate_list
                    for orders in orders1 + orders2 + orders3]

estimable_vector_inputs = [PythonEstimable(np.tile(deltas, (len(coordinate_list), 1)),
                                           np.array([cl for cl in coordinate_list]),
                                           orders) for orders in orders1 + orders2 + orders3]


@pytest.mark.parametrize("inputs", estimable_inputs + estimable_vector_inputs)
def test_python_estimable(inputs):
    # Create objects
    pmm_obj = PostManoeuvreMoment(inputs.orders)

    # Create fast_callable
    fc_test = pmm_obj.estimable(what="callable")
    fc_test_val = fc_test(inputs.deltas, inputs.x)

    # Create FunctionType, not vectorised for the sake of simplicity, apply per row
    FT_test = pmm_python_estimable(inputs.orders)
    nrows = np.atleast_2d(inputs.x).shape[0]
    FT_test_val = [FT_test(inputs.deltas[row, :], inputs.x[row, :], inputs.orders)
                   for row in range(nrows)] if nrows > 1 else FT_test(inputs.deltas, inputs.x, inputs.orders)

    # Check Python evaluations
    assert fc_test_val == pytest.approx(FT_test_val)


# Test symbolic moments
@dataclass(frozen=True)
class SymbolicMoments:
    orders: list
    sol: sage.symbolic.expression.Expression


def create_hd_moments(orders):
    """Return the symbolic expression for the hand-derived moment up to second order"""

    # Check for negative orders
    for o in orders:
        if o < 0:
            raise ValueError(f"All orders in {orders} must be non-negative.")

    # Create MGF and PMM object
    mgf_ = MomentGeneratingFunction()
    mu, Sigma = mgf_.mu, mgf_.Sigma

    pmm_ = PostManoeuvreMoment(orders=orders)
    a, b = pmm_.a, pmm_.b

    # Define symbolic one and two
    one, two = SR(1), SR(2)

    # Check if no derivative is taken
    if sum(orders) == 0:
        return mgf_.mgf

    # First order
    elif sum(orders) == 1:
        # Find variable we are differentiating
        dixi = orders.index(1)

        # Define first raw moment; this is Eq 37.
        first_raw = mu[dixi] + \
            exp(-mu[3] - one / two * (Sigma[0][0] - Sigma[3][3])) * \
            (a[dixi] * sin(mu[0] - Sigma[0][3]) + b[dixi] * cos(mu[0] - Sigma[0][3]))

        return first_raw

    elif (sum(orders) == 2) & (orders.count(2) == 1):
        # Find variable we are differentiating
        dixi = orders.index(2)

        # Define first-order variables
        xi_j = [0, 0, 0, 0]
        xi_j[dixi] = 1

        # Define second raw moment; this is Eq. (42)
        second_raw = [
            mu[dixi]**two + Sigma[dixi][dixi],
            two * a[dixi] * EV(trig="sin", n_beta=1, m_rho=1, orders=xi_j).expected_value_of(),
            two * b[dixi] * EV(trig="cos", n_beta=1, m_rho=1, orders=xi_j).expected_value_of(),
            b[dixi]**two / two * EV(trig="cos", n_beta=2, m_rho=2, orders=[0, 0, 0, 0]).expected_value_of(),
            -a[dixi]**two / two * EV(trig="cos", n_beta=2, m_rho=2, orders=[0, 0, 0, 0]).expected_value_of(),
            a[dixi] * b[dixi] * EV(trig="sin", n_beta=2, m_rho=2, orders=[0, 0, 0, 0]).expected_value_of(),
            a[dixi]**two / two * EV(trig="cos", n_beta=0, m_rho=2, orders=[0, 0, 0, 0]).expected_value_of(),
            b[dixi]**two / two * EV(trig="cos", n_beta=0, m_rho=2, orders=[0, 0, 0, 0]).expected_value_of(),
        ]

        return sum(second_raw)

    elif (sum(orders) == 2):
        # Find variables we are differentiating
        dixi = [index for index, o in enumerate(orders) if o == 1]

        # Define first-order variables
        xi_j = [0, 0, 0, 0]
        xi_j[dixi[0]] = 1
        xi_k = [0, 0, 0, 0]
        xi_k[dixi[1]] = 1

        # Define second mixed moment
        second_mixed = [
            mu[dixi[0]] * mu[dixi[1]] + Sigma[dixi[0]][dixi[1]],
            a[dixi[1]] * EV(trig="sin", n_beta=1, m_rho=1, orders=xi_j).expected_value_of(),
            b[dixi[0]] * EV(trig="cos", n_beta=1, m_rho=1, orders=xi_k).expected_value_of(),
            a[dixi[0]] * EV(trig="sin", n_beta=1, m_rho=1, orders=xi_k).expected_value_of(),
            b[dixi[1]] * EV(trig="cos", n_beta=1, m_rho=1, orders=xi_j).expected_value_of(),
            (a[dixi[0]] * a[dixi[1]] + b[dixi[0]] * b[dixi[1]]) / two *
                EV(trig="cos", n_beta=0, m_rho=2, orders=[0, 0, 0, 0]).expected_value_of(),  # noqa: E131
            (b[dixi[0]] * b[dixi[1]] - a[dixi[0]] * a[dixi[1]]) / two *
                EV(trig="cos", n_beta=2, m_rho=2, orders=[0, 0, 0, 0]).expected_value_of(),  # noqa: E131
            (a[dixi[0]] * b[dixi[1]] + a[dixi[1]] * b[dixi[0]]) / two *
                EV(trig="sin", n_beta=2, m_rho=2, orders=[0, 0, 0, 0]).expected_value_of(),  # noqa: E131
        ]

        return sum(second_mixed)
    else:
        raise NotImplementedError("Only testable up to second order")


symbolic_moment_tests = [SymbolicMoments(orders=i, sol=create_hd_moments(i)) for i in orders1 + orders2]


@pytest.mark.parametrize("inputs", symbolic_moment_tests)
def test_symbolic_moment(inputs, very_verbose):
    # Create PMM object
    pmm_obj = PostManoeuvreMoment(orders=inputs.orders, very_verbose=very_verbose)

    # Create symbolic moment
    symb_moment = pmm_obj.moment(what="symbolic")
    diff = (symb_moment - inputs.sol).expand_trig().full_simplify()
    if very_verbose:
        print()
        print(f'CAS:     {symb_moment}')
        print(f'By hand: {inputs.sol}')
        print(f'Diff:    {diff}')

    # Compare
    assert bool(diff == 0), f"symbolic result\n{symb_moment}\nis not equal to hand-derived\n{inputs.sol}"


# Test that pre-manoeuvre moments and post-manoeuvre moments are equal when the speed change is zero
@pytest.mark.parametrize("inputs", orders1 + orders2 + orders3 + orders4)
@pytest.mark.slow
def test_pre_equals_post_moment(inputs, very_verbose):
    # Create MGF and PMM object
    mgf_obj = MomentGeneratingFunction()
    pmm_obj = PostManoeuvreMoment(orders=inputs, very_verbose=very_verbose)

    # Create symbolic moment
    symb_moment = pmm_obj.moment(what="symbolic")

    # Zero speed change and zero mean for central moment
    for i in range(4):
        symb_moment = symb_moment.subs([pmm_obj.a[i] == 0, pmm_obj.b[i] == 0, mgf_obj.mu[i] == 0])

    # Check for match of pre-manoeuvre moment
    if (sum(inputs) == 1) or (sum(inputs) == 3):
        # Odd central moment is zero
        pre_manoeuvre = 0
    elif sum(inputs) == 2:
        # Get index of two if present
        if inputs.count(2) == 1:
            diff2_index = inputs.index(2)
            pre_manoeuvre = mgf_obj.Sigma[diff2_index, diff2_index]
        # Check for indices of ones
        else:
            diff_indexes = [i for i, x in enumerate(inputs) if x == 1]
            pre_manoeuvre = mgf_obj.Sigma[diff_indexes[0], diff_indexes[1]]
    elif sum(inputs) == 4:
        # Get index of four if present
        if inputs.count(4) == 1:
            diff4_index = inputs.index(4)
            pre_manoeuvre = 3*mgf_obj.Sigma[diff4_index, diff4_index]**2
        # 3 + 1
        elif inputs.count(3) == 1:
            diff3_index = inputs.index(3)
            diff_index = inputs.index(1)
            pre_manoeuvre = 3*mgf_obj.Sigma[diff3_index, diff3_index]*mgf_obj.Sigma[diff3_index, diff_index]
        # 2 + 2
        elif inputs.count(2) == 2:
            diff2_indexes = [i for i, x in enumerate(inputs) if x == 2]
            pre_manoeuvre = mgf_obj.Sigma[diff2_indexes[0], diff2_indexes[0]] * \
                mgf_obj.Sigma[diff2_indexes[1], diff2_indexes[1]] + \
                2*mgf_obj.Sigma[diff2_indexes[0], diff2_indexes[1]]**2
        # 2 + 1 + 1
        elif inputs.count(2) == 1:
            diff2_index = inputs.index(2)
            diff_indexes = [i for i, x in enumerate(inputs) if x == 1]
            pre_manoeuvre = mgf_obj.Sigma[diff2_index, diff2_index] * \
                mgf_obj.Sigma[diff_indexes[0], diff_indexes[1]] + \
                2*mgf_obj.Sigma[diff2_index, diff_indexes[0]]*mgf_obj.Sigma[diff2_index, diff_indexes[1]]
        # 1 + 1 + 1 + 1
        else:
            pre_manoeuvre = mgf_obj.Sigma[0, 1]*mgf_obj.Sigma[2, 3] + mgf_obj.Sigma[0, 2]*mgf_obj.Sigma[1, 3] + \
                            mgf_obj.Sigma[0, 3]*mgf_obj.Sigma[1, 2]
    else:
        raise NotImplementedError(f"Testing only up to order 4. The input is order {sum(inputs)}")

    # Calculate difference
    diff = (symb_moment - pre_manoeuvre).expand_trig().full_simplify()

    if very_verbose:
        print()
        print(f"CAS: {symb_moment}")
        print(f"Expected: {pre_manoeuvre}")
        print(f"Difference: {diff}")

    assert bool(diff == 0), f"symbolic result\n{symb_moment}\nis not equal to pre-manoeuvre\n{pre_manoeuvre}"


# Test printing of LaTeX moment
@pytest.mark.parametrize("inputs", symbolic_moment_tests)
def test_latex_moment(inputs, very_verbose):
    # Create PMM object
    pmm_obj = PostManoeuvreMoment(orders=inputs.orders)

    # Create LaTeX moment
    latex_moment = pmm_obj.moment(what="latex")

    # Print
    if very_verbose:
        print(latex_moment)

    # Assert it was produced
    assert latex_moment


# Dataclass for Python moment test
@dataclass
class PythonMoment:
    deltas: list | np.ndarray
    mu: list | np.ndarray
    Sigma: np.ndarray
    orders: list
    raw: bool
    integration_tol: float
    approx_tol: float


tolerances = [
    (1.0e-6, 1.0e-6),  # 1-0-0-0
    (1.0e-6, 1.0e-6),  # 0-1-0-0
    (1.0e-6, 1.0e-6),  # 0-0-1-0
    (1.0e-6, 1.0e-6),  # 0-0-0-1
    (1.0e-5, 1.0e-6),  # 2-0-0-0
    (1.0e-5, 1.0e-6),  # 0-2-0-0
    (1.0e-5, 1.0e-6),  # 0-0-2-0
    (1.0e-6, 1.0e-6),  # 0-0-0-2
    (1.0e-5, 1.0e-6),  # 1-1-0-0
    (1.0e-5, 1.0e-6),  # 1-0-1-0
    (1.0e-6, 1.0e-6),  # 1-0-0-1
    (1.0e-5, 5.0e-6),  # 0-1-1-0
    (1.0e-5, 2.0e-6),  # 0-1-0-1
    (1.0e-5, 1.0e-6),  # 0-0-1-1
    (1.0e-5, 5.0e-6),  # 3-0-0-0
    (2.0e-5, 1.0e-5),  # 0-3-0-0
    (2.0e-5, 2.0e-5),  # 0-0-3-0
    (1.0e-6, 1.0e-6),  # 0-0-0-3
    (2.0e-5, 1.0e-5),  # 2-1-0-0
    (1.0e-5, 1.0e-4),  # 2-0-1-0
    (1.0e-5, 2.0e-6),  # 2-0-0-1
    (1.0e-5, 2.0e-5),  # 1-2-0-0
    (1.0e-5, 1.0e-5),  # 1-0-2-0
    (1.0e-6, 1.0e-6),  # 1-0-0-2
    (1.0e-5, 5.0e-6),  # 0-2-1-0
    (1.0e-5, 2.0e-5),  # 0-2-0-1
    (1.0e-5, 1.0e-5),  # 0-1-2-0
    (5.0e-5, 1.0e-3),  # 0-1-0-2
    (5.0e-6, 5.0e-5),  # 0-0-2-1
    (5.0e-5, 5.0e-4),  # 0-0-1-2
    (1.0e-5, 2.0e-5),  # 1-1-1-0
    (5.0e-5, 1.0e-4),  # 1-1-0-1
    (1.0e-4, 1.0e-4),  # 1-0-1-1
    (5.0e-5, 1.0e-4),  # 0-1-1-1
    (5.0e-5, 2.0e-5),  # 4-0-0-0
    (5.0e-5, 1.0e-4),  # 0-4-0-0
    (5.0e-5, 1.0e-4),  # 0-0-4-0
    (1.0e-6, 1.0e-6),  # 0-0-0-4
    (1.0e-4, 3.0e-4),  # 3-1-0-0
    (1.0e-4, 1.0e-4),  # 3-0-1-0
    (1.0e-5, 1.0e-4),  # 3-0-0-1
    (5.0e-5, 1.0e-5),  # 1-3-0-0
    (1.0e-4, 1.0e-5),  # 1-0-3-0
    (1.0e-6, 1.0e-6),  # 1-0-0-3
    (5.0e-5, 1.0e-4),  # 0-3-1-0
    (2.0e-4, 1.0e-3),  # 0-3-0-1
    (5.0e-5, 1.0e-4),  # 0-1-3-0
    (5.0e-5, 5.0e-3),  # 0-1-0-3
    (2.0e-4, 1.0e-4),  # 0-0-3-1
    (5.0e-5, 5.0e-4),  # 0-0-1-3
    (5.0e-5, 5.0e-5),  # 2-2-0-0
    (5.0e-5, 2.0e-5),  # 2-0-2-0
    (5.0e-5, 5.0e-6),  # 2-0-0-2
    (5.0e-5, 5.0e-5),  # 0-2-2-0
    (1.0e-5, 5.0e-4),  # 0-2-0-2
    (1.0e-5, 5.0e-3),  # 0-0-2-2
    (5.0e-5, 3.0e-6),  # 2-1-1-0
    (1.0e-4, 5.0e-4),  # 2-1-0-1
    (5.0e-5, 1.0e-3),  # 2-0-1-1
    (5.0e-5, 3.0e-5),  # 1-2-1-0
    (2.0e-5, 5.0e-4),  # 1-2-0-1
    (5.0e-5, 3.0e-5),  # 1-1-2-0
    (5.0e-5, 4.0e-3),  # 1-1-0-2
    (5.0e-5, 3.0e-4),  # 1-0-2-1
    (5.0e-5, 5.0e-3),  # 1-0-1-2
    (2.0e-4, 3.0e-5),  # 0-2-1-1
    (2.0e-4, 3.0e-4),  # 0-1-2-1
    (5.0e-5, 5.0e-4),  # 0-1-1-2
    (1.0e-4, 5.0e-4),  # 1-1-1-1
]


_rng = np.random.default_rng(314)
test_Sigma = _rng.uniform(low=0, high=0.1, size=(4, 4)) + np.eye(4)

moment_vector_inputs = [PythonMoment(np.array(deltas),
                                     make_lpc_for_test(100000, 150000, 10, -5),
                                     np.dot(test_Sigma.T, test_Sigma),
                                     orders,
                                     True,
                                     accuracy,
                                     tolerance)
                        for orders, (accuracy, tolerance) in zip(orders1 + orders2 + orders3 + orders4, tolerances)]


def extract_MD(M, orders):
    """
    Extracts the element of the multi-dimensional tensor of moments M specified by order.

    Parameters
    ----------
    M : np.ndarray
        The tensor. Must be fully symmetric, e.g, in 2D case M[i, j] == M[j, i] for any i, j
    orders : np.ndarray
        The orders of the moment to extract from M.

    Returns
    -------
    float
        The desired element.

    """
    T = np.expand_dims(M, -1)
    for o in range(4):
        for _ in range(orders[o]):
            T = T[o, :]
    return T[0]


class TestExtractMD:
    def test_1d(self):
        # Has 4 independent values
        M = [0, 1, 2, 3]
        for pos in range(4):
            orders = [0, 0, 0, 0]
            orders[pos] += 1
            val = extract_MD(M, orders)
            assert val == pytest.approx(M[pos])

    def test_2d(self):
        # Has 10 independent values
        M = np.array([[0, 1, 2, 3],
                      [1, 4, 5, 6],
                      [2, 5, 7, 8],
                      [3, 6, 8, 9]])
        for pos0 in range(4):
            for pos1 in range(4):
                orders = [0, 0, 0, 0]
                orders[pos0] += 1
                orders[pos1] += 1
                val = extract_MD(M, orders)
                assert val == pytest.approx(M[pos0, pos1])

    def test_3d(self):
        # Has 20 independent values
        M = np.full((4, 4, 4), fill_value=np.nan)
        M[0, 0, 0:] = [0, 1, 2, 3]
        M[0, 1, 1:] = [4, 5, 6]
        M[0, 2, 2:] = [7, 8]
        M[0, 3, 3:] = [9]
        M[1, 1, 1:] = [10, 11, 12]
        M[1, 2, 2:] = [13, 14]
        M[1, 3, 3:] = [15]
        M[2, 2, 2:] = [16, 17]
        M[2, 3, 3:] = [18]
        M[3, 3, 3:] = [19]
        for p0 in range(4):
            for p1 in range(4):
                for p2 in range(4):
                    if np.isnan(M[p0, p1, p2]):
                        o = sorted([p0, p1, p2])
                        M[p0, p1, p2] = M[o[0], o[1], o[2]]

        for p0 in range(4):
            for p1 in range(4):
                for p2 in range(4):
                    orders = [0, 0, 0, 0]
                    orders[p0] += 1
                    orders[p1] += 1
                    orders[p2] += 1
                    val = extract_MD(M, orders)
                    assert val == pytest.approx(M[p0, p1, p2])


@pytest.mark.parametrize("inputs", moment_vector_inputs,
                         ids=['-'.join([str(v) for v in mvi.orders]) for mvi in moment_vector_inputs])
@pytest.mark.slow
def test_python_moment(inputs, very_verbose):
    fc_test = post_manoeuvre.moment(orders=inputs.orders)
    fc_test_val = fc_test(inputs.deltas, inputs.mu, inputs.Sigma)

    if very_verbose:
        print()
        print(f"Testing order: {np.array(inputs.orders)}")
        print(f'Delta-v: {inputs.deltas}')
        print(f'Pre-manoeuvre:\n    mean:\n{inputs.mu}\n    covariance:\n{inputs.Sigma}')
        print(f"Expected: {fc_test_val}")

    # Underlying Gaussian
    true_distribution = qp.Gaussian(qp.DigitalNetB2(4, seed=24), inputs.mu, inputs.Sigma)

    # Make integrand
    pmm_obj = PostManoeuvreMoment(orders=inputs.orders)
    estimable = pmm_obj.estimable(what='callable')
    integrand = qp.CustomFun(true_distribution, lambda x: estimable(inputs.deltas, x))

    # Integrate
    computed_value, data = qp.CubBayesNetG(integrand=integrand,
                                           rel_tol=inputs.integration_tol,
                                           abs_tol=inputs.integration_tol).integrate()
    del data

    mism = fc_test_val - computed_value
    mid = (fc_test_val + computed_value) / 2

    if very_verbose:
        print(f"Computed: {computed_value}")
        print(f'Mismatch: absolute {mism}, relative {mism / mid} to the value of {mid}')

    assert fc_test_val == pytest.approx(computed_value, rel=inputs.approx_tol, abs=inputs.approx_tol)

    gc.collect()


@pytest.fixture
def exporter():
    script = sagedir / 'post-manoeuvre-moments.sage'
    highest_order = 3

    reference = sagedir.parent / 'post_manoeuvre' / 'impl'
    assert reference.exists()

    orders = get_Nth_orders(highest_order)
    submodules = []
    for order in orders:
        suffix = ''.join([str(o) for o in order])
        submodule = reference / f'moment_{suffix}.py'
        assert submodule.exists()
        submodules.append(submodule)

    return (script, highest_order, reference, submodules)


class TestExportScript:
    def _read_code(self, path_):
        code = []
        with open(path_, 'rt') as ifile:
            for line in ifile:
                line = line.strip()
                if not line.startswith("#"):
                    code.append(line.rstrip())
        return code

    @pytest.mark.slow
    def test_invoke(self, tmp_path, exporter):
        script, highest_order, reference, submodules = exporter

        output_folder = tmp_path / 'pmm'
        command_line = [
            'sage',
            str(script),
            '--output-folder', str(output_folder),
            '-N', str(highest_order),
            '--verbose',
        ]
        kwargs = {
            'capture_output': True,
            'text': True,
        }

        result = subprocess.run(command_line, **kwargs)
        if result.returncode:
            error_message = f"""
exit status {result.returncode} from
command:
    {command_line}
with messages:
    stdout:
{result.stdout}
    stderr:
{result.stderr}
"""
            raise RuntimeError(error_message)

        assert (output_folder / '__init__.py').exists()
        assert (output_folder / 'impl' / '__init__.py').exists()

        for submodule in submodules:
            ref_code = self._read_code(submodule)
            name = submodule.name
            generated = output_folder / 'impl' / name
            test_code = self._read_code(generated)
            assert len(ref_code) == len(test_code), f'submodule {name} differs in the number of non-comment lines'
            diff = [(r, t) for r, t in zip(ref_code, test_code) if r != t]
            mismatch = '\n'.join(['reference:\n    {r}\ngenerated:\n    {t}' for (r, t) in diff])
            assert not diff, f'submodule {name}, differences:\n{mismatch}'
