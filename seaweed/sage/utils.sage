from sage.all import *
from dataclasses import dataclass
from enum import Enum
from typing import Sequence, Optional
import numpy as np
import itertools

sage.repl.load.load('mgf.sage', globals())


def expand_trig_expression(f, x):
    """Given a trigonometic function, write all powers of trigonometric function as
    linear cominbations of terms of the form sin(n*x) and cos(n*x), where n is an integer

    Parameter
    ---------
    f: sage.symbolic.expression.Expression
        function of x, of the form f(x) = c1*sin(m_sin * x)**a_sin_pwr + c2*cos(n_cos * x)**b_cos_pwr
    x: sage.symbolic.expression.Expression
        variable pertaining to these coefficients

    Return
    ------
    f_simple: sage.symbolic.expression.Expression
        reduced form of function
    """

    return f.trig_reduce(var=x).expand()


# Define trig type
class TrigType(Enum):
    COSINE = 0
    SINE = 1


# Define dataclasses for terms
@dataclass
class TrigTerm:
    trig: TrigType
    power: int
    coefficient: int


# Combine to form operand
@dataclass(eq=False)
class Operand:
    multiplier: sage.symbolic.expression.Expression
    sine: Optional[TrigTerm] = None
    cosine: Optional[TrigTerm] = None

    def __eq__(self, other):
        if not isinstance(other, Operand):
            return NotImplemented
        if self.sine and other.sine:
            return (self.sine.power, self.sine.coefficient) == (other.sine.power, other.sine.coefficient)
        elif self.cosine and other.cosine:
            return (self.cosine.power, self.cosine.coefficient) == (other.cosine.power, other.cosine.coefficient)
        else:
            sm = SR(self.multiplier)
            om = SR(other.multiplier)
            return bool(sm.subs(dict(zip(sm.variables(), np.repeat(1, len(sm.variables()))))) ==
                       (om.subs(dict(zip(om.variables(), np.repeat(1, len(om.variables())))))))

    def __gt__(self, other):
        if not isinstance(other, Operand):
            return NotImplemented
        if self.sine and other.sine:
            return (self.sine.power, self.sine.coefficient) > (other.sine.power, other.sine.coefficient)
        elif self.cosine and other.cosine:
            return (self.cosine.power, self.cosine.coefficient) > (other.cosine.power, other.cosine.coefficient)
        else:
            sm = SR(self.multiplier)
            om = SR(other.multiplier)
            return bool(sm.subs(dict(zip(sm.variables(), np.repeat(1, len(sm.variables()))))) >
                       (om.subs(dict(zip(om.variables(), np.repeat(1, len(om.variables())))))))


# Class for variable and its power
@dataclass(eq=False)
class Power:
    power: int
    multiplier: sage.symbolic.expression.Expression

    def __eq__(self, other):
        if not isinstance(other, Power):
            return NotImplemented
        return self.multiplier == other.multiplier

    def __gt__(self, other):
        if not isinstance(other, Power):
            return NotImplemented
        return self.multiplier > other.multiplier


def get_trigonometric_coefficients(f, x, very_verbose: bool = False):
    """Given a trigonometric function, obtain the trigonometric coefficients within

    Parameters
    ----------
    f: sage.symbolic.expression.Expression
        function of x, of the form f(x) = c1*sin(m_sin * x) + c2*cos(n_cos * x)
    x: sage.symbolic.expression.Expression
        variable pertaining to these coefficients

    Return
    ------
    coefficient_list: list
        for each term, return a list of Operands
    """

    # Simplify initial function
    f = expand_trig_expression(f, x)

    # Get powers and coefficients
    power_list = get_trigonometric_powers(f, x, very_verbose)

    # Initialise list
    coefficient_list = []

    # Loop through and check that no trigonometric powers or mixed products are present
    for term in power_list:
        # Check powers have been reduced
        if (term.sine and term.sine.power > 1) or \
           (term.cosine and term.cosine.power > 1) or \
           (term.sine and term.cosine and term.sine.power * term.cosine.power != 0):
            raise RuntimeError(f"Term {term} contains trigonometric powers that have not been reduced.")
        else:
            coefficient_list.append(term)

    return coefficient_list


def get_trigonometric_powers(f, x, very_verbose: bool = False):
    """Given a trigonometric function, obtain the trigonometric coefficients and powers within

    Parameters
    ----------
    f: sage.symbolic.expression.Expression
        function of x, of the form f(x) = c1*sin(m_sin * x)**a_sin_pwr + c2*cos(n_cos * x)**b_cos_pwr
    x: sage.symbolic.expression.Expression
        variable pertaining to these coefficients

    Return
    ------
    coefficient_list: list
        for each term, return a list of Operands
    """

    # Initialise list
    coefficient_list = []

    # Print initial function
    if very_verbose:
        print(f'--------\n{f}\n--------')

    # Check if the expression is a sum. If not, make it iterable anyway, for consistency in implementation
    if f.operator() is sage.symbolic.operators.add_vararg:
        ops = f.operands()
    else:
        ops = [f]

    # Define maximum order possible
    # From Eq. 47 and 48 of expectation.tex, for sin(m*b)^c, the largest possible coefficient once expanded using
    #   the power reduction formulae is sin((c + 1)*m*beta)

    # Initialise power and coefficient
    max_pwr = 0
    max_coef = 0

    # Iterate through operands fo find maximum order
    for op in ops:
        for fl in op.factor_list():
            # Append power of factor
            max_pwr = max(max_pwr, fl[1])

            # Check for trig coefficient
            if (fl[0].operator() == cos) | (fl[0].operator() == sin):
                max_coef = max(max_coef, fl[0].simplify_trig().degree(cos(x)), fl[0].simplify_trig().degree(sin(x)))
            else:
                max_coef = max(max_coef, 1)

    max_coef_total = (max_pwr + 1) * max_coef

    # Define list of trig functions
    sine_list = [sin(p*x) for p in range(1, max_coef_total + 1)]
    cosine_list = [cos(p*x) for p in range(1, max_coef_total + 1)]

    # Loop through operands
    for op in ops:
        if very_verbose:
            print(f'operand {op}: {op.factor_list()}')

        # Initialise coefficients and powers
        m_sin = 0
        a_sin_pwr = 0
        n_cos = 0
        b_cos_pwr = 0
        coef = 1

        # Loop through factors
        for g, pwr in op.factor_list():
            if very_verbose:
                print(f'    examine g: {g}, pwr: {pwr}')

            if (g not in sine_list) & (g not in cosine_list):
                coef *= g**pwr
                if very_verbose:
                    print(f'    -> not trig, {pwr} is just a power of {g}')
            else:
                # Loop through powers
                for p in range(len(sine_list)):
                    # Check for trigonometric functions
                    if g == sine_list[p]:
                        if very_verbose:
                            print(f'    -> {g} is a sine of {p + 1} with power {pwr}')
                        a_sin_pwr = pwr
                        m_sin = p + 1
                    if g == cosine_list[p]:
                        if very_verbose:
                            print(f'    -> {g} is a cosine of {p + 1} with power {pwr}')
                        b_cos_pwr = pwr
                        n_cos = p + 1

        # Create operand
        if m_sin > 0:
            Op_sin = TrigTerm(TrigType.SINE, power=a_sin_pwr, coefficient=m_sin)
        else:
            Op_sin = None

        if n_cos > 0:
            Op_cos = TrigTerm(TrigType.COSINE, power=b_cos_pwr, coefficient=n_cos)
        else:
            Op_cos = None

        Op = Operand(sine=Op_sin,
                     cosine=Op_cos,
                     multiplier=coef)

        # Append to list
        if very_verbose:
            print(f'    ==> write {coef} into {(m_sin, a_sin_pwr, n_cos, b_cos_pwr)}')
        coefficient_list.append(Op)

    if very_verbose:
        print()

    return coefficient_list


def get_power_of(f, x, very_verbose: bool = False):
    """Given a function, look for powers of x and return a list of Power objects

    Parameters
    ----------
    f: sage.symbolic.expression.Expression
        function of r
    x: sage.symbolic.expression.Expression
        variable pertaining to powers (e.g. range)
    very_verbose: bool
        if True, print extra output

    Return
    ------
    power_list: list
        for each term, return a list of Powers
    """

    # Initialise list
    power_list = []

    # Print initial function
    if very_verbose:
        print(f'--------\n{f}\n--------')

    # Check if the expression is a sum. If not, make it iterable for consistency
    if f.operator() is sage.symbolic.operators.add_vararg:
        ops = f.operands()
    else:
        ops = [f]

    # Loop through operands
    for op in ops:
        if very_verbose:
            print(f'operand {op}: {op.factor_list()}')

        # Initialise power and coefficient
        x_pwr = 0
        coef = 1

        # Loop through factors
        for g, pwr in op.factor_list():
            if very_verbose:
                print(f'    examine g: {g}, pwr: {pwr}')

            if (g.has(x)) and (g.degree(x) != 0):
                # Check for x power
                if very_verbose:
                    print(f'    -> {g} is a function of {x} with power {pwr}')
                x_pwr += pwr
            else:
                coef *= g**pwr
                if very_verbose:
                    print(f'    -> not trig, {pwr} is just a power of {g}')

        # Create operand
        x_obj = Power(multiplier=coef, power=x_pwr)

        # Add to list
        if very_verbose:
            print(f'    ==> write {coef} into {(x_pwr)}')
        power_list.append(x_obj)

    if very_verbose:
        print()

    return power_list


def get_orders_of(expr: sage.symbolic.expression.Expression,
                  variables: Sequence[sage.symbolic.expression.Expression],
                  powers: Optional[list] = None) -> list:
    """Given a list of variables, extract the degrees of each variable in expr and return as a list.

    Parameters
    ----------
    expr: sage.symbolic.expression.Expression
        expression of interest
    variables: list
        list of variables to search for
    powers: list
        list of powers for each variable to store

    Return
    ------
    powers: list
        list of powers of each variable in variables
    coefficient: sage.symbolic.expression.Expression
        coefficient of all variables
    """

    # Initialise list
    if powers is None:
        powers = []

    # Call first variable
    var0 = variables[0]
    powers0 = get_power_of(expr, var0)

    # Check length is one
    assert len(powers0) == 1, f"Expression is a sum: {expr}"
    powers0 = powers0[0]

    # Convert to SR if coefficient is an integer
    coefficient = SR(powers0.multiplier)

    # Check coefficient is not a sum
    assert coefficient.expand().operator() is not sage.symbolic.operators.add_vararg, \
        f"{coefficient.expand().operator()} is a sum."

    # Check variable of interest is not present
    assert (not coefficient.has(var0)) | bool(coefficient.degree(var0) == 0), \
        f"{var0} is still present in {coefficient}."

    # Save power
    powers.append(powers0.power)

    # Remove checked variable from list and call recursively until list is empty
    if len(variables) > 1:
        powers, expr = get_orders_of(coefficient, variables[1:], powers)

    powers_final = get_power_of(expr, var0)
    expr = SR(powers_final[0].multiplier)

    return powers, expr


def create_EV(Op: Operand, Pwr: Power, orders: list):
    """Given an Operand, Power, and orders, form an EV object

    Parameters
    ----------
    Op: Operand
        object containing information about sine and cosine
    Pwr: Power
        object containing information about power of range
    orders: list
        list containing information about powers of xi

    Return
    ------
    ev: EV
        object combining the parameters
    """

    # Get trig function
    if Op.sine:
        trig, n_beta = "sin", Op.sine.coefficient
    elif Op.cosine:
        trig, n_beta = "cos", Op.cosine.coefficient
    else:
        trig, n_beta = "cos", 0

    # Create EV
    return EV(trig=trig, n_beta=n_beta, m_rho=-Pwr.power, orders=orders)


def get_Nth_orders(N: int) -> list:
    """Given an integer, N, return all orders of differentiation that sum to N
    for a quadrivariate Gaussian distribution

    Parameter
    ---------
    N: int
        Maximum order of differentiation

    Return
    ------
    orders: list
        All orders of differentiation that sum to N
    """

    # Get all possible sums of N
    possible_sums = []

    onetoN = range(1, N + 1)

    for i in range(4):
        for j in list(itertools.combinations_with_replacement(onetoN, i+1)):
            if (sum(j) == N):
                possible_sums.append(list(j))

    # Pad with zeros to make at least length 4
    for ps in possible_sums:
        ps += [0] * (4 - len(ps))

    # Get all permutations
    orders = [sorted(set(list(itertools.permutations(ps))), reverse=True) for ps in possible_sums]

    # Flatten list and convert tuples to lists
    orders = [list(i) for j in orders for i in j]

    return orders
