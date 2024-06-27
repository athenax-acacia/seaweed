"""Creates and differentiates the moment-generating function (MGF) for a
multivariate normal distribution with N=4"""

import numpy as np
import itertools
import collections
import copy
from dataclasses import dataclass
from typing import Sequence, Tuple


@dataclass(frozen=True)
class EV:
    """Data class for components of a given expected value"""
    trig: str  # sine or cosine
    n_beta: int  # bearing multiplier
    m_rho: int  # scaled range rate multiplier
    orders: Sequence[sage.rings.integer.Integer]  # orders of differentiation

    def __post_init__(self):
        """Checks inputs for dataclass are valid"""
        # Check for appropriate trig
        if self.trig not in ["sin", "cos"]:
            raise ValueError(f"{self.trig} is not a trigonometric function.")

        # Check multipliers are non-negative
        if self.n_beta < 0:
            raise ValueError(f"Bearing multiplier {self.n_beta} must be non-negative.")

        if self.m_rho < 0:
            raise ValueError(f"Range scale {self.m_rho} must be non-negative.")

        # Check orders of differentiation are sensible
        if not isinstance(self.orders, Sequence):
            raise TypeError(f'attribute {self.orders} is not a Sequence')
        if len(self.orders) != 4:
            raise ValueError(f'sequence {self.orders} is not of length 4')
        for el in self.orders:
            if (not isinstance(el, sage.rings.integer.Integer)) & \
               (not isinstance(el, int)) & \
               (not isinstance(el, sage.symbolic.expression.Expression)):
                raise TypeError(f'element {el} is not an int or SR')
            if el < 0:
                raise ValueError(f'element {el} is negative')

    @classmethod
    def unwrap(cls, orders: list) -> Sequence[int]:
        """
        Presents the derivative as a sequence. Given

                   \\partial^3 \\Phi
            -----------------------------------
            \\partial^2 \\xi_0 \\partial \\xi_2

        unwrap each differentiation explicitly:

                            \\partial^3 \\Phi
            = --------------------------------------------------
              \\partial \\xi_0 \\partial \\xi_0 \\partial \\xi_2

        and interchange the order of differentiation

                            \\partial^3 \\Phi
            = --------------------------------------------------
              \\partial \\xi_2 \\partial \\xi_0 \\partial \\xi_0

        to produce the final output:

            -> [2, 0, 0]

        Return
        ------
        Sequence[int]
            Indices of variables that the function is differentiated upon, sorted in
            non-increasing order.

        """

        # Repeat each index by the number of differentiations
        li = [[c] * orders[c] for c in range(4)]
        rv = list(itertools.chain(*li))

        # Sort descendingly
        rv.sort(reverse=True)

        return rv

    @classmethod
    def rebuild(cls, elements: Sequence[int]) -> Sequence[int]:
        """Converts a sequence of differentiation into an orders attribute"""

        ctr = collections.Counter({i: 0 for i in range(4)})
        ctr.update(collections.Counter(elements))

        # Check for indices beyond length of state space
        if len(ctr) != 4:
            raise ValueError(f'elements in {elements} are outside of 0...3 range')

        return [ctr[i] for i in range(4)]

    def make_latex(self):
        """Prints as a LaTeX expression"""
        # Create symbolic expression and convert to LaTeX
        r = var('r')
        beta = var('beta')

        expr = latex(r^(-self.m_rho)*self.trig(self.n_beta*beta))

        # Complete expression for expected value
        E = "$\\mathbb{E} \\left[" + expr + "\\right]$"

        return E

    def make_str(self):
        """Prints as readable string"""
        # Initialise expression for expected value
        E = ["E["]

        for index, o in enumerate(self.orders):
            if o > 0:
                if o == 1:
                    E.append(f'xi{index}')
                else:
                    E.append(f'xi{index}^{o}')

        if self.m_rho:
            E.append(f"r^{-self.m_rho}")

        if self.n_beta:
            if self.n_beta > 1:
                E.append(f"{self.trig}({self.n_beta} beta)")
            else:
                E.append(f"{self.trig}(beta)")

        E.append("]")
        return " ".join(E)

    def _expected_value_of_0(self, real_part: bool):
        """
        Returns real or imaginary part of Eq. 43 that gives E[r^-m exp(+/-i n*beta)], where i = sqrt(-1).
        """

        # Initialise MGF object for mu and Sigma
        mgf = MomentGeneratingFunction()
        mu, Sigma = mgf.mu, mgf.Sigma

        # Define base (real)
        base_real = exp(-self.m_rho * mu[3] - 1/2 * (self.n_beta**2 * Sigma[0][0] - self.m_rho**2 * Sigma[3][3]))

        # Define function within trig
        inside_trig = self.n_beta * mu[0] - self.m_rho * self.n_beta * Sigma[0][3]

        # Choose real or imaginary part
        return base_real * cos(inside_trig) if real_part else base_real * sin(inside_trig)

    def _expected_value_of_1(self, j: int, real_part: bool):
        """
        Returns real or imaginary part of Eq. 44 that gives E[xi_j * r^-m exp(+/-i n*beta)],
        where j is an integer, and i = sqrt(-1).
        """

        # Initialise MGF object for mu and Sigma
        mgf = MomentGeneratingFunction()
        mu, Sigma = mgf.mu, mgf.Sigma

        # Real and imaginary parts of the pre-exponential term and the complex exponent
        otr, oti = mu[j] - self.m_rho * Sigma[3][j], self.n_beta * Sigma[0][j]
        er, ei = self._expected_value_of_0(real_part=True), self._expected_value_of_0(real_part=False)

        # Choose real or imaginary part
        return (otr * er - oti * ei) if real_part else (otr * ei + oti * er)

    def expected_value_of(self):
        """Recursive implementation of the known expressions for expected value"""

        if (self.orders == [0, 0, 0, 0]):
            return self._expected_value_of_0(self.trig == "cos")
        elif (sum(self.orders) == 1):
            return self._expected_value_of_1(self.orders.index(1), self.trig == "cos")
        else:
            # Initialise MGF object for mu and Sigma
            mgf = MomentGeneratingFunction()
            mu, Sigma = mgf.mu, mgf.Sigma

            # Recursively obtain differentiation
            heads, tail = recurse(self.orders)

            # Define expected value
            sign = SR(-1) if self.trig == "sin" else SR(1)
            expected_value = (mu[tail.k] +
                              (Sigma[tail.k]).inner_product(vector([sign * self.n_beta, 0, 0, self.m_rho]))) * \
                EV(self.trig, n_beta=self.n_beta, m_rho=self.m_rho, orders=tail.ev).expected_value_of()

            # Add head terms
            for head in heads:
                expected_value += Sigma[head.kj[0]][head.kj[1]] \
                    * EV(trig=self.trig, n_beta=self.n_beta, m_rho=self.m_rho, orders=head.ev).expected_value_of()

            return expected_value


# Define dataclass Eq 52 terms
@dataclass(frozen=True)
class Tail:
    """
    The class representing the final term in Eq. (52)
    """
    k: int
    ev: list


@dataclass(frozen=True)
class Head:
    """
    The class representing the leading (sum) terms in Eq. (52)
    """
    kj: Tuple[int, int]
    ev: list


def recurse(ev: list) -> Tuple[Sequence[Head], Tail]:
    """
    Implement Eq. (52)

    Parameters
    ----------
    ev : list
        The description of the input derivative on the lhs of Eq. (52).

    Returns
    -------
    (Tuple[Sequence[Head], Tail])
        The terms on the rhs of Eq. (52): a sequence of the Head terms plus one Tail.

    """

    # Unwrap into sequence
    li = EV.unwrap(ev)

    # Obtain first order
    k = li.pop(0)

    # Create counter list
    ctr = collections.Counter(li)

    m2s = []
    for el in li:
        # Make copy of counter
        ctr_1 = copy.copy(ctr)

        # Update counter
        ctr_1[el] -= 1

        # Add Head instance and rebuilt EV differentiation sequence
        m2s.append(Head((k, el), EV.rebuild(ctr_1)))

    # Return Tail
    return (m2s, Tail(k, EV.rebuild(ctr)))


class MomentGeneratingFunction():
    """Class for defining the moment-generating function.

    Attributes
    ----------
    h: 4x1 vector
        variable of the MGF
    x: 4x1 vector
        state space in LPC
    mu: 4x1 vector
        mean of the multivariate normal distribution
    Sigma: 4x4 matrix
        covariance matrix of the multivariate normal distribution
    mgf: symbolic expression
        moment-generating function

    Method
    ------
    __init__(self)
        Create the class attributes
    """

    def __init__(self):
        # Define h, state space, and mean vectors, assuming the latter two are real
        self.h = vector(var(','.join(f'h{i}' for i in range(4))))

        beta, beta_dot, rho_dot, rho, r = var('beta, beta_dot, rho_dot, rho, r', domain="real")
        self.x = vector([beta, beta_dot, rho_dot, rho])
        self.mu = vector(var(','.join(f"mu{i}" for i in range(4)), domain="real"))

        # Create symmetric covariance matrix
        Sigma = var(','.join(f"sigma_{i}{j}" for i in range(4) for j in range(4)), domain="real")
        Sigma = Matrix(4, 4, Sigma)
        Sigma = np.tril(Sigma) + np.triu(Sigma.T, 1)
        self.Sigma = Matrix(Sigma)

        # Define mgf function
        self.mgf = exp((self.mu * self.h.column() + 1/2 * self.h * self.Sigma * self.h.column())[0])
