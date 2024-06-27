# Testing for sage utils

# Import packages
import pytest
import warnings
from dataclasses import dataclass
from pathlib import Path

# Skip all these tests if sage isn't installed in the environment
sage = pytest.importorskip('sage', reason="Sage is not installed")
warnings.filterwarnings("ignore")
from sage.all import *

# Set wd
project_root = Path(__file__).parents[1]
sagedir = project_root/'sage'
load_attach_path(str(sagedir))
sage.repl.load.load('utils.sage', globals())


# Test get_trigonometric_coefficients
@dataclass(frozen=True)
class TrigonometricCoefficients:
    f: sage.symbolic.expression.Expression
    x: sage.symbolic.expression.Expression
    sol: list


# Initialise variables
x, a, b, r = var('x, a, b, r')

# Create list of tests
trigonometric_coefficient_tests = [TrigonometricCoefficients(f=sin(x), x=x,
                                                             sol=[Operand(sine=TrigTerm(trig=TrigType.SINE,
                                                                                        power=1,
                                                                                        coefficient=1),
                                                                          multiplier=1)]),
                                   TrigonometricCoefficients(f=cos(x), x=x,
                                                             sol=[Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=1),
                                                                          multiplier=1)]),
                                   TrigonometricCoefficients(f=-sin(x), x=x,
                                                             sol=[Operand(sine=TrigTerm(trig=TrigType.SINE,
                                                                                        power=1,
                                                                                        coefficient=1),
                                                                          multiplier=-1)]),
                                   TrigonometricCoefficients(f=1/2*cos(x), x=x,
                                                             sol=[Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=1),
                                                                          multiplier=0.5)]),
                                   TrigonometricCoefficients(f=4*sin(2*x)**2*cos(4*x)**3, x=x,
                                                             sol=[Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=16),
                                                                          multiplier=-0.25),
                                                                  Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=12),
                                                                          multiplier=0.5),
                                                                  Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=8),
                                                                          multiplier=-1),
                                                                  Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=4),
                                                                          multiplier=1.5),
                                                                  Operand(multiplier=-0.75)]),
                                   TrigonometricCoefficients(f=2*sin(5*x) + 9*sin(5*x), x=x,
                                                             sol=[Operand(sine=TrigTerm(trig=TrigType.SINE,
                                                                                        power=1,
                                                                                        coefficient=5),
                                                                          multiplier=11)]),
                                   TrigonometricCoefficients(f=a*sin(2*x)**4 + b*cos(8*x)**3 + a*b, x=x,
                                                             sol=[Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=4),
                                                                          multiplier=-0.5*a),
                                                                  Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=24),
                                                                          multiplier=0.25*b),
                                                                  Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=8),
                                                                          multiplier=0.125*a),
                                                                  Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=8),
                                                                          multiplier=0.75*b),
                                                                  Operand(multiplier=a*b),
                                                                  Operand(multiplier=0.375*a)]),
                                   TrigonometricCoefficients(f=r**-2*cos(5*x)*3*a, x=x,
                                                             sol=[Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=5),
                                                                          multiplier=3*a*r**-2)]),
                                   TrigonometricCoefficients(f=r**-1*sin(4*x)**2*cos(5*x)*r**0*r**-5*22, x=x,
                                                             sol=[Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=13),
                                                                          multiplier=-11/2*r**-6),
                                                                  Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=5),
                                                                          multiplier=11*r**-6),
                                                                  Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                          power=1,
                                                                                          coefficient=3),
                                                                          multiplier=-11/2*r**-6)]),
                                   TrigonometricCoefficients(f=x, x=x,
                                                             sol=[Operand(multiplier=x)])]


@pytest.mark.parametrize("inputs", trigonometric_coefficient_tests)
def test_get_trigonometric_coefficients(inputs):
    # Run function
    test_gtc = get_trigonometric_coefficients(inputs.f, inputs.x)

    # Sort lists
    sorted_test_gtc = sorted(test_gtc)
    sorted_sol = sorted(inputs.sol)

    # Compare
    assert sorted_test_gtc == sorted_sol, f'''Mismatched list of Operands.sorted_sol
                                              The computed list has unexpected elements:
                                              {[i for i in sorted_test_gtc if i not in sorted_sol]}.\n
                                              The expected list has unexpected elements:
                                              {[i for i in sorted_sol if i not in sorted_test_gtc]}.'''


# Test get_trigonometric_powers
# Initialise tests equal to get_trigonometric_coefficients
trigonometric_power_tests = trigonometric_coefficient_tests[:]

# Manually correct non-expanded
trigonometric_power_tests[4] = TrigonometricCoefficients(f=4*sin(2*x)**2*cos(4*x)**3, x=x,
                                                         sol=[Operand(sine=TrigTerm(trig=TrigType.SINE,
                                                                                    power=2,
                                                                                    coefficient=2),
                                                                      cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                      power=3,
                                                                                      coefficient=4),
                                                                      multiplier=4)])
trigonometric_power_tests[6] = TrigonometricCoefficients(f=a*sin(2*x)**4 + b*cos(8*x)**3 + a*b, x=x,
                                                         sol=[Operand(sine=TrigTerm(trig=TrigType.SINE,
                                                                                    power=4,
                                                                                    coefficient=2),
                                                                      multiplier=a),
                                                              Operand(cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                      power=3,
                                                                                      coefficient=8),
                                                                      multiplier=b),
                                                              Operand(multiplier=a*b)])
trigonometric_power_tests[8] = TrigonometricCoefficients(f=r**-1*sin(4*x)**2*cos(5*x)*r**0*r**-5*22, x=x,
                                                         sol=[Operand(sine=TrigTerm(trig=TrigType.SINE,
                                                                                    power=2,
                                                                                    coefficient=4),
                                                                      cosine=TrigTerm(trig=TrigType.COSINE,
                                                                                      power=1,
                                                                                      coefficient=5),
                                                                      multiplier=22*r**-6)])


@pytest.mark.parametrize("inputs", trigonometric_power_tests)
def test_get_trigonometric_powers(inputs):
    # Run function
    test_gtp = get_trigonometric_powers(inputs.f, inputs.x)

    # Sort lists
    sorted_test_gtp = sorted(test_gtp)
    sorted_p_sol = sorted(inputs.sol)

    # Compare
    assert sorted_test_gtp == sorted_p_sol, f'''Mismatched list of Operands.sorted_sol
                                              The computed list has unexpected elements:
                                              {[i for i in sorted_test_gtp if i not in sorted_p_sol]}.\n
                                              The expected list has unexpected elements:
                                              {[i for i in sorted_p_sol if i not in sorted_test_gtp]}.'''


# Create tests for finding powers of x
@dataclass(frozen=True)
class TestPower:
    f: sage.symbolic.expression.Expression
    x: sage.symbolic.expression.Expression
    sol: list


get_power_of_tests = [TestPower(f=b, x=r, sol=[Power(power=0, multiplier=b)]),
                      TestPower(f=a*r**-5, x=r, sol=[Power(power=-5, multiplier=a)]),
                      TestPower(f=23*r**-2*r**-3, x=r, sol=[Power(power=-5, multiplier=23)]),
                      TestPower(f=5*a/r, x=r, sol=[Power(power=-1, multiplier=5*a)]),
                      TestPower(f=sin(r), x=r, sol=[Power(power=0, multiplier=sin(r))]),
                      TestPower(f=5/(r**2) + 6*cos(4*x)/(r**3), x=r, sol=[Power(power=-2, multiplier=5),
                                                                          Power(power=-3, multiplier=6*cos(4*x))]),
                      TestPower(f=5/r + 6/r, x=r, sol=[Power(power=-1, multiplier=11)])]


@pytest.mark.parametrize("inputs", get_power_of_tests)
def test_range_power(inputs):
    # Run function
    test_po = get_power_of(inputs.f, inputs.x)

    # Sort lists
    sorted_test_po = sorted(test_po)
    sorted_x_sol = sorted(inputs.sol)

    # Compare
    assert sorted_test_po == sorted_x_sol, f'''Mismatched list of Power.sorted_sol
                                              The computed list has unexpected elements:
                                              {[i for i in sorted_test_po if i not in sorted_x_sol]}.\n
                                              The expected list has unexpected elements:
                                              {[i for i in sorted_x_sol if i not in sorted_test_po]}.'''


# Test get_orders_of
@dataclass(frozen=True)
class TestGetOrders:
    expr: sage.symbolic.expression.Expression
    variables: list
    powers: list
    multiplier: sage.symbolic.expression.Expression


# Create input tests
ys = list(var(','.join(f'y{i}' for i in range(4))))
get_order_of_tests = [TestGetOrders(expr=5*y0, variables=ys, powers=[1, 0, 0, 0], multiplier=SR(5)),
                      TestGetOrders(expr=12*b*y1**2*y3, variables=ys, powers=[0, 2, 0, 1], multiplier=12*b),
                      TestGetOrders(expr=SR(50), variables=ys, powers=[0, 0, 0, 0], multiplier=SR(50)),
                      TestGetOrders(expr=y0**4 * y1**3 * y2**2 * y3**10, variables=ys,
                                    powers=[4, 3, 2, 10], multiplier=SR(1)),
                      TestGetOrders(expr=5*sin(y0)*y2**5, variables=ys,
                                    powers=[0, 0, 5, 0], multiplier=5*sin(y0))]


@pytest.mark.parametrize("inputs", get_order_of_tests)
def test_get_order_of(inputs, very_verbose):
    # Run function
    powers, multiplier = get_orders_of(expr=inputs.expr, variables=inputs.variables)

    # Check powers
    if very_verbose:
        print()
        print(f'CAS:     {powers}')
        print(f'Expected: {inputs.powers}')

    assert powers == inputs.powers, f"CAS {powers} does not equal expected {inputs.powers}."

    # Check multipliers
    if very_verbose:
        print()
        print(f'CAS:     {multiplier}')
        print(f'Expected: {inputs.multiplier}')

    assert bool(multiplier - inputs.multiplier == 0), \
        f"CAS {multiplier} does not equal expected {inputs.multiplier}."


# Test create_EV
@dataclass
class TestEV:
    Op: Operand
    Pwr: Power
    orders: list
    EV_sol: EV


# Define variables
variables = vector(var(','.join(f'y{i}' for i in range(4))))


create_ev_tests = [TestEV(Op=Operand(sine=TrigTerm(trig=TrigType.SINE, power=1, coefficient=4),
                                     multiplier=2*y0),
                          Pwr=Power(power=-1, multiplier=2),
                          orders=[1, 0, 0, 0],
                          EV_sol=EV(trig="sin", n_beta=4, m_rho=1, orders=[1, 0, 0, 0])),
                   TestEV(Op=Operand(cosine=TrigTerm(trig=TrigType.COSINE, power=1, coefficient=3),
                                     multiplier=2*y0**2*y1*2),
                          Pwr=Power(power=-3, multiplier=1),
                          orders=[2, 1, 0, 0],
                          EV_sol=EV(trig="cos", n_beta=3, m_rho=3, orders=[2, 1, 0, 0])),
                   TestEV(Op=Operand(sine=TrigTerm(trig=TrigType.SINE, power=1, coefficient=2),
                                     multiplier=24*a),
                          Pwr=Power(power=-4, multiplier=2),
                          orders=[0, 0, 0, 0],
                          EV_sol=EV(trig="sin", n_beta=2, m_rho=4, orders=[0, 0, 0, 0])),
                   TestEV(Op=Operand(sine=TrigTerm(trig=TrigType.SINE, power=4, coefficient=5),
                                     multiplier=2*y0**2*y1**3*y2**4*y3**10),
                          Pwr=Power(power=-3, multiplier=1),
                          orders=[2, 3, 4, 10],
                          EV_sol=EV(trig="sin", n_beta=5, m_rho=3, orders=[2, 3, 4, 10]))]


@pytest.mark.parametrize("inputs", create_ev_tests)
def test_create_ev(inputs):
    # Run function
    computed_ev = create_EV(inputs.Op, inputs.Pwr, inputs.orders)

    # Check for equality
    assert computed_ev == inputs.EV_sol, f"Computed {computed_ev} does not match expected {inputs.EV_sol}."


# Testing for generating all orders of order N
@dataclass
class NthOrder:
    N: int
    expected: list | int


# Initialise orders from 1 to 4
orders1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
orders2 = [[2, 0, 0, 0],
           [0, 2, 0, 0],
           [0, 0, 2, 0],
           [0, 0, 0, 2],
           [1, 1, 0, 0],
           [1, 0, 1, 0],
           [1, 0, 0, 1],
           [0, 1, 1, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 1]]
orders3 = [[3, 0, 0, 0],
           [0, 3, 0, 0],
           [0, 0, 3, 0],
           [0, 0, 0, 3],
           [2, 1, 0, 0],
           [2, 0, 1, 0],
           [2, 0, 0, 1],
           [1, 2, 0, 0],
           [0, 2, 1, 0],
           [0, 2, 0, 1],
           [1, 0, 2, 0],
           [0, 1, 2, 0],
           [0, 0, 2, 1],
           [1, 0, 0, 2],
           [0, 1, 0, 2],
           [0, 0, 1, 2],
           [1, 1, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 1],
           [0, 1, 1, 1]]
orders4 = [[4, 0, 0, 0],
           [0, 4, 0, 0],
           [0, 0, 4, 0],
           [0, 0, 0, 4],
           [3, 1, 0, 0],
           [3, 0, 1, 0],
           [3, 0, 0, 1],
           [1, 3, 0, 0],
           [0, 3, 1, 0],
           [0, 3, 0, 1],
           [1, 0, 3, 0],
           [0, 1, 3, 0],
           [0, 0, 3, 1],
           [1, 0, 0, 3],
           [0, 1, 0, 3],
           [0, 0, 1, 3],
           [2, 1, 1, 0],
           [2, 1, 0, 1],
           [2, 0, 1, 1],
           [1, 2, 1, 0],
           [1, 2, 0, 1],
           [0, 2, 1, 1],
           [1, 1, 2, 0],
           [1, 0, 2, 1],
           [0, 1, 2, 1],
           [1, 1, 0, 2],
           [1, 0, 1, 2],
           [0, 1, 1, 2],
           [2, 2, 0, 0],
           [2, 0, 2, 0],
           [2, 0, 0, 2],
           [0, 2, 2, 0],
           [0, 2, 0, 2],
           [0, 0, 2, 2],
           [1, 1, 1, 1]]
orders5 = [[5, 0, 0, 0],
           [0, 5, 0, 0],
           [0, 0, 5, 0],
           [0, 0, 0, 5],
           [4, 1, 0, 0],
           [4, 0, 1, 0],
           [4, 0, 0, 1],
           [1, 4, 0, 0],
           [0, 4, 1, 0],
           [0, 4, 0, 1],
           [1, 0, 4, 0],
           [0, 1, 4, 0],
           [0, 0, 4, 1],
           [1, 0, 0, 4],
           [0, 1, 0, 4],
           [0, 0, 1, 4],
           [3, 2, 0, 0],
           [3, 0, 2, 0],
           [3, 0, 0, 2],
           [2, 3, 0, 0],
           [0, 3, 2, 0],
           [0, 3, 0, 2],
           [2, 0, 3, 0],
           [0, 2, 3, 0],
           [0, 0, 3, 2],
           [2, 0, 0, 3],
           [0, 2, 0, 3],
           [0, 0, 2, 3],
           [3, 1, 1, 0],
           [3, 1, 0, 1],
           [3, 0, 1, 1],
           [1, 3, 1, 0],
           [1, 3, 0, 1],
           [0, 3, 1, 1],
           [1, 1, 3, 0],
           [1, 0, 3, 1],
           [0, 1, 3, 1],
           [1, 1, 0, 3],
           [1, 0, 1, 3],
           [0, 1, 1, 3],
           [2, 2, 1, 0],
           [2, 2, 0, 1],
           [2, 1, 2, 0],
           [2, 1, 0, 2],
           [2, 0, 2, 1],
           [2, 0, 1, 2],
           [1, 2, 2, 0],
           [1, 2, 0, 2],
           [1, 0, 2, 2],
           [0, 2, 2, 1],
           [0, 2, 1, 2],
           [0, 1, 2, 2],
           [2, 1, 1, 1],
           [1, 2, 1, 1],
           [1, 1, 2, 1],
           [1, 1, 1, 2]]
orders6 = [[6, 0, 0, 0],
           [0, 6, 0, 0],
           [0, 0, 6, 0],
           [0, 0, 0, 6],
           [5, 1, 0, 0],
           [5, 0, 1, 0],
           [5, 0, 0, 1],
           [1, 5, 0, 0],
           [1, 0, 5, 0],
           [1, 0, 0, 5],
           [0, 5, 1, 0],
           [0, 5, 0, 1],
           [0, 1, 5, 0],
           [0, 1, 0, 5],
           [0, 0, 5, 1],
           [0, 0, 1, 5],
           [4, 2, 0, 0],
           [4, 0, 2, 0],
           [4, 0, 0, 2],
           [2, 4, 0, 0],
           [2, 0, 4, 0],
           [2, 0, 0, 4],
           [0, 4, 2, 0],
           [0, 4, 0, 2],
           [0, 2, 4, 0],
           [0, 2, 0, 4],
           [0, 0, 4, 2],
           [0, 0, 2, 4],
           [3, 3, 0, 0],
           [3, 0, 3, 0],
           [3, 0, 0, 3],
           [0, 3, 3, 0],
           [0, 3, 0, 3],
           [0, 0, 3, 3],
           [4, 1, 1, 0],
           [4, 1, 0, 1],
           [4, 0, 1, 1],
           [1, 4, 1, 0],
           [1, 4, 0, 1],
           [1, 1, 4, 0],
           [1, 1, 0, 4],
           [1, 0, 4, 1],
           [1, 0, 1, 4],
           [0, 4, 1, 1],
           [0, 1, 4, 1],
           [0, 1, 1, 4],
           [3, 2, 1, 0],
           [3, 2, 0, 1],
           [3, 1, 2, 0],
           [3, 1, 0, 2],
           [3, 0, 2, 1],
           [3, 0, 1, 2],
           [2, 3, 1, 0],
           [2, 3, 0, 1],
           [2, 1, 3, 0],
           [2, 1, 0, 3],
           [2, 0, 3, 1],
           [2, 0, 1, 3],
           [1, 3, 2, 0],
           [1, 3, 0, 2],
           [1, 2, 3, 0],
           [1, 2, 0, 3],
           [1, 0, 3, 2],
           [1, 0, 2, 3],
           [0, 3, 2, 1],
           [0, 3, 1, 2],
           [0, 2, 3, 1],
           [0, 2, 1, 3],
           [0, 1, 3, 2],
           [0, 1, 2, 3],
           [2, 2, 2, 0],
           [2, 2, 0, 2],
           [2, 0, 2, 2],
           [0, 2, 2, 2],
           [3, 1, 1, 1],
           [1, 3, 1, 1],
           [1, 1, 3, 1],
           [1, 1, 1, 3],
           [2, 2, 1, 1],
           [2, 1, 2, 1],
           [2, 1, 1, 2],
           [1, 2, 2, 1],
           [1, 2, 1, 2],
           [1, 1, 2, 2]]

orders_tests = [orders1, orders2, orders3, orders4, orders5, orders6]

testable_1_6_order = [NthOrder(i, orders_tests[i-1]) for i in range(1, 7)]


@pytest.mark.parametrize("inputs", testable_1_6_order)
def test_get_Nth_orders(inputs):
    # Get all orders
    automated_orders = get_Nth_orders(inputs.N)

    # Sort lists
    sorted_automated_orders = sorted(automated_orders)
    sorted_manual_orders = sorted(inputs.expected)

    # Mismatches
    mismatch1 = [i for i in sorted_automated_orders if i not in sorted_manual_orders]
    mismatch2 = [i for i in sorted_manual_orders if i not in sorted_automated_orders]

    # Compare
    assert sorted_automated_orders == sorted_manual_orders, f'''Mismatched list of orders
                                                                The computed list has unexpected elements:
                                                                {mismatch1}.\n
                                                                The expected list has unexpected elements:
                                                                {mismatch2}.'''
