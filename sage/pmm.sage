"""Take mixed partial derivatives of the moment-generating function and export
to various forms."""

import numpy as np
import itertools
from typing import Sequence, Optional

from sage.all import *
sage.repl.load.load('mgf.sage', globals())
sage.repl.load.load('utils.sage', globals())


class PostManoeuvreMoment:
    """Class for defining the moments of the post-manoeuvre distribution using the moment generating function (MGF)."

    Attributes
    ----------
    h: 4x1 vector
        variable of the MGF
    x: 4x1 vector
        state space in LPC
    a: 4x1 vector
        coefficients of sine terms
    b: 4x1 vector
        coefficients of cosine terms
    xi: 4x1 vector
        generic state space variables
    orders: 4x1 vector
        orders of differentiation

    Methods
    -------
    __init__(self, orders)
        Create the class attributes

    _delta_representation(self)
        Substitute values for a and b in self.pmm

    estimable(self, what)
        Given a string for the type of object, return the estimable PMM

    moment(self, what)
        Given a string for the type of object, return the closed-form moment
    """

    def __init__(self, orders, very_verbose: bool = False):
        self._very_verbose = very_verbose
        # Define h and state space
        self.h = vector(var(','.join(f'h{i}' for i in range(4))))

        beta, beta_dot, rho_dot, rho, r = var('beta, beta_dot, rho_dot, rho, r', domain="real")
        self.x = vector([beta, beta_dot, rho_dot, rho])

        # Define constant coefficients for trigonometric functions
        self.a = [var(f"a_{i}", domain="real", latex_name=f"a_{{{i}}}") for i in range(4)]
        self.b = [var(f"b_{i}", domain="real", latex_name=f"b_{{{i}}}") for i in range(4)]
        self.xi = [var(f"xi_{i}", domain="real", latex_name=f"\\xi_{{{i}}}") for i in range(4)]

        # Stop function if orders vector and h vector have unequal lengths
        if (len(self.h) != len(orders)):
            raise ValueError(f'self.h length {len(self.h)} != orders length {len(orders)}')

        # Stop if any derivatives are negative
        if sum(o < 0 for o in orders):
            raise ValueError(f'Cannot take negative derivatives! {orders}')

        # Define orders of differentiation
        self.orders = orders

        # Define post-manoeuvre moment symbolic expressions
        self.pmm = 1
        for o in range(4):
            self.pmm = self.pmm * (self.xi[o] + self.a[o] * np.sin(beta)/r + self.b[o] * np.cos(beta)/r) ^ (self.orders[o])

        # Define representations of derivatives
        self._method = {}

        self._method['estimable'] = {}
        self._method['moment'] = {}

        # Adding elements one at a time
        for k in ['symbolic', 'latex', 'callable']:
            self._method['estimable'][k] = None
            self._method['moment'][k] = None
        self._method['moment']['python'] = None

    def _delta_representation(self, expr):
        """Converts given trigonometric coefficients into components of velocity

        Parameter
        ---------
        expr: sage.symbolic.expression.Expression
            expression to substitute into

        Return
        ------
        pmm_np: sage.symbolic.expression.Expression
            post-manoeuvre product as Python code
        """

        # Define symbolic variables with manual LaTeX representation since Python won't allow spaces
        delta_v = vector(var(f'delta_v{i}', latex_name=f'\\Delta v_{i}') for i in range(4))
        x = vector(var(','.join(f'x{i}' for i in range(4))))

        # Define coefficients
        a = vector([0, delta_v[1], -delta_v[0], 0])
        b = vector([0, -delta_v[0], -delta_v[1], 0])

        # Python vector
        pmm_np = expr
        for o in range(4):
            if self.orders[o] > 0:
                pmm_np = pmm_np.subs([self.xi[o] == x[o], self.a[o] == a[o], self.b[o] == b[o]])

        # Substitute functions
        pmm_np = pmm_np.subs([x[0] == var('beta'), x[3] == np.log(var('r'))])

        # Return product
        return pmm_np

    def estimable(self, what: str):
        """Creates an integrand of the requested type

        Parameters
        ----------
        what: str
            one of "symbolic", "latex" or "callable"

        Return
        ------
        estimable: str
            either a sage symbolic expression, LaTeX expression, or valid Python code
        """
        # TODO but likely not: for consistency with moments, we can also export estimables as pure
        # Python functions (what='python'); however, this is a "nice to have" feature at best.
        # First, the estimables obtained below as `fast_callable` are fast enough, there is no need
        # to speed things up. Second, and more importantly, the estimables are only for internal
        # usage: they are meant to be used in verifying the moments by direct numerical integration.
        # The end users need the moments, not the estimables. Thus, we probably can skip exporing
        # the estimables into pure Python. This "to-do" note is preserved to explain the rationale
        # and effectively is a "not to-do" note.

        if (what == 'symbolic'):
            if self._method['estimable']['symbolic'] is None:
                self._method['estimable']['symbolic'] = self.pmm
            return self._method['estimable']['symbolic']
        elif (what == 'latex'):
            if self._method['estimable']['latex'] is None:
                self._method['estimable']['latex'] = latex(self.pmm)
            return self._method['estimable']['latex']
        elif (what == 'callable'):
            if self._method['estimable']['callable'] is None:
                pmm_delta = self._delta_representation(self.pmm)
                pmm_delta = pmm_delta.subs(beta=x0, r=exp(x3))
                func = fast_callable(pmm_delta, vars=[delta_v0, delta_v1, x0, x1, x2, x3])

                def _unpack(delta_v, x):
                    dv = np.atleast_2d(delta_v)
                    x = np.atleast_2d(x)
                    assert dv.shape[1] == 2
                    assert x.shape[1] == 4
                    return np.squeeze(func(dv[:, 0], dv[:, 1], x[:, 0], x[:, 1], x[:, 2], x[:, 3]))

                self._method['estimable']['callable'] = _unpack
            return self._method['estimable']['callable']
        else:
            raise ValueError(f'unknown argument {what}, not one of ["symbolic", "latex", "callable"]')

    def moment(self, what: str):
        """Creates an expression for the closed-form moment of the requested type

        Parameters
        ----------
        what: str
            one of "symbolic", "latex", "callable" or "python"

        Return
        ------
        moment: str
            either a sage symbolic expression, LaTeX expression, fast_callable or valid Python code
        """

        def _symbolic_moment():
            # Expand and simplify
            pmm_expanded = expand_trig_expression(self.pmm, var('beta'))

            # Decompose PMM into Operand objects
            Ops = get_trigonometric_coefficients(pmm_expanded, var('beta'),
                                                 very_verbose=self._very_verbose)

            # For each Operand, get the range terms: list of lists of length 1; then flatten it
            Range_ops = [get_power_of(op.multiplier, var('r'),
                                      very_verbose=self._very_verbose) for op in Ops]
            Range_ops = list(itertools.chain.from_iterable(Range_ops))

            # Assert the lengths are equal (all terms have been accounted for, no grouping)
            assert len(Ops) == len(Range_ops), f"Ops has length {len(Ops)}, but Range_ops has length {len(Range_ops)}."

            # Check that all leading coefficients do not contain beta or r
            for r_op in Range_ops:
                if (r_op.multiplier.has(var('r'))):
                    raise ValueError(f"The multiplier {r_op.multiplier} contains a scaled range.")

                if (r_op.multiplier.has(var('beta'))):
                    raise ValueError(f"The multiplier {r_op.multiplier} contains bearing.")

            # Call for Range_ops
            Xi_ops = [get_orders_of(variables=list(self.xi), expr=r_op.multiplier) for r_op in Range_ops]

            # Get coefficients and separate from Xi powers
            coeffs = [i[1] for i in Xi_ops]
            Xi_ops = [i[0] for i in Xi_ops]

            # Obtain parameters for EV object
            EVs = [create_EV(*i) for i in zip(Ops, Range_ops, Xi_ops)]

            # Check length is equal
            assert len(EVs) == len(coeffs), f"There are {len(EVs)} EVs but {len(coeffs)} coefficients."

            # Create expression
            expr = 0

            for j in range(len(EVs)):
                expr += coeffs[j] * EVs[j].expected_value_of()

            return expr

        if (what == 'symbolic'):
            if self._method['moment']['symbolic'] is None:
                self._method['moment']['symbolic'] = _symbolic_moment()
            return self._method['moment']['symbolic']
        elif (what == 'latex'):
            # TODO or nice-to-have: we could use the delta representation for deriving the symbolic
            # moments in the first place. As tested with LaTeX, the change significantly decreases
            # the number of terms to carry along, and therefore, can be a notable speed-up of the
            # symbolic computations. However, in the ultimate design we do not export moments just
            # in time. Instead they are generated once and committed to git. Therefore, there is no
            # need to speed things up.
            pmm_delta = self._delta_representation(self.moment(what='symbolic'))
            self._method['moment']['latex'] = latex(pmm_delta)
            return self._method['moment']['latex']
        elif (what == 'callable'):
            pmm_delta = self._delta_representation(self.moment(what='symbolic'))

            func = fast_callable(pmm_delta, vars=[delta_v0, delta_v1,
                                                  mu0, mu1, mu2, mu3,
                                                  sigma_00, sigma_10, sigma_20, sigma_30,
                                                  sigma_11, sigma_21, sigma_31,
                                                  sigma_22, sigma_32,
                                                  sigma_33])

            def _unpack(delta_v, mu, sigma):
                dv = np.atleast_2d(delta_v)
                mu = np.atleast_2d(mu)
                sigma = np.atleast_3d(sigma)
                assert dv.shape[1] == 2
                assert mu.shape[1] == 4
                # behaviour of atleast_3d differs from atleast_2d, e.g., see
                # https://stackoverflow.com/questions/43612024/behavior-of-numpy-atleast-3d
                assert sigma.shape[0] == 4
                assert sigma.shape[1] == 4
                return np.squeeze(func(dv[:, 0], dv[:, 1],
                                       mu[:, 0], mu[:, 1], mu[:, 2], mu[:, 3],
                                       sigma[0, 0, :], sigma[0, 1, :], sigma[0, 2, :], sigma[0, 3, :],
                                       sigma[1, 1, :], sigma[1, 2, :], sigma[1, 3, :],
                                       sigma[2, 2, :], sigma[2, 3, :],
                                       sigma[3, 3, :]))

            self._method['moment']['callable'] = _unpack
            return self._method['moment']['callable']
        elif (what == 'python'):
            pmm_delta = self._delta_representation(self.moment(what='symbolic'))

            from yapf.yapflib.yapf_api import FormatCode
            orders_s = ''.join([str(int(o)) for o in self.orders])
            pmm_delta_s = str(pmm_delta._sympy_())
            delta_v_s = '\n'.join([f'    delta_v{i} = delta_v[{i}]' for i in range(2)
                                   if pmm_delta.has(var(f'delta_v{i}'))])
            mu_s = '\n'.join([f'    mu{i} = mu[{i}]' for i in range(4)
                              if pmm_delta.has(var(f'mu{i}'))])
            sigma_s = '\n'.join([f'    sigma_{i}{j} = sigma[{i}, {j}]' for i in range(4) for j in range(4)
                                 if pmm_delta.has(var(f'sigma_{i}{j}'))])
            code = f'''import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_{orders_s}(delta_v, mu, sigma):
    delta_v = np.atleast_1d(delta_v)
    mu = np.atleast_1d(mu)
    sigma = np.atleast_2d(sigma)

    assert delta_v.shape == (2,)
    assert mu.shape == (4,)
    assert sigma.shape == (4, 4)

{delta_v_s}
{mu_s}
{sigma_s}

    return {pmm_delta_s}
'''
            formatted_code, _ = FormatCode(code)
            self._method['moment']['python'] = formatted_code
            return self._method['moment']['python']
        else:
            raise ValueError(f'unknown argument {what}, not one of ["symbolic", "latex", "callable", "python"]')
