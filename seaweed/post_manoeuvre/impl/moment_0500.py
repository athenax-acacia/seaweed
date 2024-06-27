# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 0,5,0,0
# to recreate, then copy the file 'moment_0500.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_0500(delta_v, mu, sigma):
    delta_v = np.atleast_1d(delta_v)
    mu = np.atleast_1d(mu)
    sigma = np.atleast_2d(sigma)

    assert delta_v.shape == (2, )
    assert mu.shape == (4, )
    assert sigma.shape == (4, 4)

    delta_v0 = delta_v[0]
    delta_v1 = delta_v[1]
    mu0 = mu[0]
    mu1 = mu[1]
    mu3 = mu[3]
    sigma_00 = sigma[0, 0]
    sigma_10 = sigma[1, 0]
    sigma_11 = sigma[1, 1]
    sigma_30 = sigma[3, 0]
    sigma_31 = sigma[3, 1]
    sigma_33 = sigma[3, 3]

    return -delta_v0**5 * exp(
        -5 * mu3 - 25 * sigma_00 / 2 + 25 * sigma_33 / 2
    ) * cos(5 * mu0 - 25 * sigma_30) / 16 - 5 * delta_v0**5 * exp(
        -5 * mu3 - 9 * sigma_00 / 2 + 25 * sigma_33 / 2
    ) * cos(3 * mu0 - 15 * sigma_30) / 16 - 5 * delta_v0**5 * exp(
        -5 * mu3 - sigma_00 / 2 + 25 * sigma_33 /
        2) * cos(mu0 - 5 * sigma_30) / 8 + 5 * delta_v0**4 * delta_v1 * exp(
            -5 * mu3 - 25 * sigma_00 / 2 + 25 * sigma_33 / 2) * sin(
                5 * mu0 - 25 * sigma_30
            ) / 16 + 15 * delta_v0**4 * delta_v1 * exp(
                -5 * mu3 - 9 * sigma_00 / 2 + 25 * sigma_33 / 2
            ) * sin(
                3 *
                mu0
                - 15 * sigma_30
            ) / 16 + 5 * delta_v0**4 * delta_v1 * exp(
                -5 * mu3 - sigma_00 /
                2 +
                25 * sigma_33 / 2
            ) * sin(
                mu0
                -
                5 *
                sigma_30
            ) / 8 + 15 * delta_v0**4 * (
                mu1
                - 4
                * sigma_31
            ) * exp(
                -4 * mu3 +
                8 *
                sigma_33
            ) / 8 + 5 * delta_v0**4 * (
                -4 * sigma_10 *
                exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                * sin(4 * mu0 - 16 * sigma_30)
                + (mu1 - 4 * sigma_31)
                * exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                * cos(4 * mu0 - 16 * sigma_30)
            ) / 8 + 5 * delta_v0**4 * (
                -2 * sigma_10 *
                exp(-4 * mu3 - 2 * sigma_00 + 8 * sigma_33)
                * sin(2 * mu0 - 8 * sigma_30)
                + (mu1 - 4 * sigma_31)
                * exp(-4 * mu3 - 2 * sigma_00 + 8 * sigma_33)
                * cos(2 * mu0 - 8 * sigma_30)
            ) / 2 + 5 * delta_v0**3 * delta_v1**2 * exp(
                -5 * mu3 -
                25 * sigma_00 /
                2 +
                25 * sigma_33 /
                2
            ) * cos(
                5 *
                mu0
                - 25 * sigma_30
            ) / 8 + 5 * delta_v0**3 * delta_v1**2 * exp(
                -5 * mu3 - 9 * sigma_00 / 2 + 25 * sigma_33 / 2
            ) * cos(
                3 *
                mu0
                - 15 * sigma_30
            ) / 8 - 5 * delta_v0**3 * delta_v1**2 * exp(
                -5 * mu3 -
                sigma_00 / 2 + 25 *
                sigma_33 / 2
            ) * cos(
                mu0
                -
                5 *
                sigma_30
            ) / 4 - 5 * delta_v0**3 * delta_v1 * (
                4 *
                sigma_10 * exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                * cos(4 * mu0 - 16 * sigma_30)
                + (mu1 - 4 * sigma_31)
                * exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                * sin(4 * mu0 - 16 * sigma_30)
            ) / 2 - 5 * delta_v0**3 * delta_v1 * (
                2 *
                sigma_10 * exp(-4 * mu3 - 2 * sigma_00 + 8 * sigma_33)
                * cos(2 * mu0 - 8 * sigma_30)
                + (mu1 - 4 * sigma_31)
                * exp(-4 * mu3 - 2 * sigma_00 + 8 * sigma_33)
                * sin(2 * mu0 - 8 * sigma_30)
            ) - 5 * delta_v0**3 * (
                sigma_11 * exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33 / 2)
                * cos(3 * mu0 - 9 * sigma_30)
                + (-3 * sigma_10 *
                   exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33 / 2)
                   * sin(3 * mu0 - 9 * sigma_30)
                   +
                   (mu1 - 3 * sigma_31)
                   * exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33 / 2)
                   * cos(3 * mu0 - 9 * sigma_30))
                * (mu1 + 3 * sigma_10 + 3 * sigma_31)
            ) / 2 - 15 * delta_v0**3 * (
                sigma_11 * exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2)
                * cos(mu0 - 3 * sigma_30)
                + (-sigma_10 * exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2)
                   * sin(mu0 - 3 * sigma_30)
                   + (mu1 - 3 * sigma_31)
                   * exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2)
                   * cos(mu0 - 3 * sigma_30))
                * (mu1 + sigma_10 + 3 * sigma_31)
            ) / 2 - 5 * delta_v0**2 * delta_v1**3 * exp(
                -5 * mu3 -
                25 * sigma_00 /
                2 +
                25 * sigma_33 / 2
            ) * sin(
                5 *
                mu0
                - 25 * sigma_30
            ) / 8 + 5 * delta_v0**2 * delta_v1**3 * exp(
                -5 * mu3 - 9 *
                sigma_00 / 2 +
                25 * sigma_33 /
                2
            ) * sin(
                3 *
                mu0
                - 15 * sigma_30
            ) / 8 + 5 * delta_v0**2 * delta_v1**3 * exp(
                -5 * mu3 -
                sigma_00 / 2 +
                25 * sigma_33 /
                2
            ) * sin(
                mu0 -
                5 *
                sigma_30
            ) / 4 + 15 * delta_v0**2 * delta_v1**2 * (
                mu1
                - 4 * sigma_31
            ) * exp(
                -4 * mu3 +
                8 *
                sigma_33
            ) / 4 - 15 * delta_v0**2 * delta_v1**2 * (
                -4 * sigma_10 *
                exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                * sin(4 * mu0 - 16 * sigma_30)
                + (mu1 - 4 * sigma_31)
                * exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                * cos(4 * mu0 - 16 * sigma_30)
            ) / 4 + 15 * delta_v0**2 * delta_v1 * (
                sigma_11 * exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33 / 2)
                * sin(3 * mu0 - 9 * sigma_30)
                + (3 * sigma_10 *
                   exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33 / 2)
                   * cos(3 * mu0 - 9 * sigma_30)
                   +
                   (mu1 - 3 * sigma_31)
                   * exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33 / 2)
                   * sin(3 * mu0 - 9 * sigma_30))
                * (mu1 - 3 * sigma_10 + 3 * sigma_31)
            ) / 2 + 15 * delta_v0**2 * delta_v1 * (
                sigma_11 * exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2)
                * sin(mu0 - 3 * sigma_30)
                + (sigma_10 * exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2) *
                   cos(mu0 - 3 * sigma_30)
                   + (mu1 - 3 * sigma_31)
                   * exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2)
                   * sin(mu0 - 3 * sigma_30))
                * (mu1 - sigma_10 + 3 * sigma_31)
            ) / 2 + 5 * delta_v0**2 * (
                2 *
                sigma_11 *
                (-2 * sigma_10 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                 sin(2 * mu0 - 4 * sigma_30)
                 + (mu1 - 2 * sigma_31)
                 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33)
                 * cos(2 * mu0 - 4 * sigma_30))
                +
                (sigma_11 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                 cos(2 * mu0 - 4 * sigma_30)
                 +
                 (-2 * sigma_10 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                  sin(2 * mu0 - 4 * sigma_30)
                  + (mu1 - 2 * sigma_31)
                  * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33)
                  * cos(2 * mu0 - 4 * sigma_30))
                 * (mu1 + 2 * sigma_10 + 2 * sigma_31))
                * (mu1 + 2 * sigma_10 + 2 * sigma_31)
            ) + 5 * delta_v0**2 * (
                2 *
                sigma_11 * (mu1 - 2 * sigma_31)
                * exp(-2 * mu3 + 2 * sigma_33)
                + (mu1 + 2 * sigma_31)
                * (sigma_11 * exp(-2 * mu3 + 2 * sigma_33) +
                   (mu1 - 2 * sigma_31)
                   * (mu1 + 2 * sigma_31)
                   * exp(-2 * mu3 + 2 * sigma_33))
            ) - 5 * delta_v0 * delta_v1**4 * exp(
                -5 * mu3 -
                25 * sigma_00 / 2 +
                25 * sigma_33 / 2
            ) * cos(
                5 *
                mu0
                - 25 * sigma_30
            ) / 16 + 15 * delta_v0 * delta_v1**4 * exp(
                -5 * mu3 - 9 *
                sigma_00 / 2 +
                25 * sigma_33 / 2
            ) * cos(
                3 *
                mu0
                - 15 * sigma_30
            ) / 16 - 5 * delta_v0 * delta_v1**4 * exp(
                -5 * mu3 -
                sigma_00 / 2 +
                25 * sigma_33 / 2
            ) * cos(
                mu0 -
                5 *
                sigma_30
            ) / 8 + 5 * delta_v0 * delta_v1**3 * (
                4 *
                sigma_10 * exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                * cos(4 * mu0 - 16 * sigma_30)
                + (mu1 - 4 * sigma_31)
                * exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                * sin(4 * mu0 - 16 * sigma_30)
            ) / 2 - 5 * delta_v0 * delta_v1**3 * (
                2 * sigma_10 * exp(-4 * mu3 - 2 * sigma_00 + 8 * sigma_33)
                * cos(2 * mu0 - 8 * sigma_30)
                + (mu1 - 4 * sigma_31)
                * exp(-4 * mu3 - 2 * sigma_00 + 8 * sigma_33)
                * sin(2 * mu0 - 8 * sigma_30)
            ) + 15 * delta_v0 * delta_v1**2 * (
                sigma_11 * exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33 / 2)
                * cos(3 * mu0 - 9 * sigma_30)
                + (-3 * sigma_10 *
                   exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33 / 2)
                   * sin(3 * mu0 - 9 * sigma_30)
                   + (mu1 - 3 * sigma_31)
                   * exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33 / 2)
                   * cos(3 * mu0 - 9 * sigma_30))
                * (mu1 + 3 * sigma_10 + 3 * sigma_31)
            ) / 2 - 15 * delta_v0 * delta_v1**2 * (
                sigma_11 * exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2)
                * cos(mu0 - 3 * sigma_30)
                +
                (-sigma_10 * exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2) *
                 sin(mu0 - 3 * sigma_30)
                 + (mu1 - 3 * sigma_31)
                 * exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2)
                 * cos(mu0 - 3 * sigma_30))
                * (mu1 + sigma_10 + 3 * sigma_31)
            ) / 2 - 10 * delta_v0 * delta_v1 * (
                2 * sigma_11 *
                (2 * sigma_10 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                 cos(2 * mu0 - 4 * sigma_30)
                 +
                 (mu1 - 2 * sigma_31) *
                 exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33)
                 * sin(2 * mu0 - 4 * sigma_30))
                +
                (sigma_11 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                 sin(2 * mu0 - 4 * sigma_30)
                 +
                 (2 * sigma_10 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                  cos(2 * mu0 - 4 * sigma_30)
                  + (mu1 - 2 * sigma_31)
                  * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33)
                  * sin(2 * mu0 - 4 * sigma_30))
                 * (mu1 - 2 * sigma_10 + 2 * sigma_31))
                * (mu1 - 2 * sigma_10 + 2 * sigma_31)
            ) - 5 * delta_v0 * (
                3 * sigma_11 *
                (sigma_11 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2)
                 * cos(mu0 - sigma_30) +
                 (-sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                  sin(mu0 - sigma_30) +
                  (mu1 - sigma_31) * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2)
                  * cos(mu0 - sigma_30)) *
                 (mu1 + sigma_10 + sigma_31)) +
                (2 * sigma_11 *
                 (-sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                  sin(mu0 - sigma_30) +
                  (mu1 - sigma_31) * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2)
                  * cos(mu0 - sigma_30)) +
                 (sigma_11 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                  cos(mu0 - sigma_30) +
                  (-sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                   sin(mu0 - sigma_30) +
                   (mu1 - sigma_31) * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2)
                   * cos(mu0 - sigma_30)) *
                  (mu1 + sigma_10 + sigma_31)) *
                 (mu1 + sigma_10 + sigma_31)) * (mu1 + sigma_10 + sigma_31)
            ) + delta_v1**5 * exp(
                -5 * mu3 - 25 * sigma_00 / 2 +
                25 * sigma_33 / 2) * sin(
                    5 * mu0 - 25 * sigma_30
                ) / 16 - 5 * delta_v1**5 * exp(
                    -5 * mu3 - 9 *
                    sigma_00 / 2 + 25 * sigma_33 / 2) * sin(
                        3 * mu0 - 15 * sigma_30) / 16 + 5 * delta_v1**5 * exp(
                            -5 * mu3 -
                            sigma_00 / 2 + 25 *
                            sigma_33 / 2
                        ) * sin(mu0 - 5 * sigma_30) / 8 + 15 * delta_v1**4 * (
                            mu1 - 4 * sigma_31
                        ) * exp(
                            -4 * mu3 + 8 * sigma_33) / 8 + 5 * delta_v1**4 * (
                                -4 * sigma_10 *
                                exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                                * sin(4 * mu0 - 16 * sigma_30) +
                                (mu1 - 4 * sigma_31) *
                                exp(-4 * mu3 - 8 * sigma_00 + 8 * sigma_33)
                                * cos(4 * mu0 - 16 * sigma_30)
                            ) / 8 - 5 * delta_v1**4 * (
                                -2 * sigma_10 *
                                exp(-4 * mu3 - 2 * sigma_00 + 8 * sigma_33)
                                * sin(2 * mu0 - 8 * sigma_30) +
                                (mu1 - 4 * sigma_31) *
                                exp(-4 * mu3 - 2 * sigma_00 + 8 * sigma_33) *
                                cos(2 * mu0 - 8 * sigma_30)
                            ) / 2 - 5 * delta_v1**3 * (
                                sigma_11 * exp(-3 * mu3 - 9 * sigma_00 / 2 +
                                               9 * sigma_33 / 2) *
                                sin(3 * mu0 - 9 * sigma_30) +
                                (3 * sigma_10 * exp(-3 * mu3 - 9 * sigma_00 /
                                                    2 + 9 * sigma_33 / 2) *
                                 cos(3 * mu0 - 9 * sigma_30) +
                                 (mu1 - 3 * sigma_31) *
                                 exp(-3 * mu3 - 9 * sigma_00 / 2 + 9 * sigma_33
                                     / 2) * sin(3 * mu0 - 9 * sigma_30)) *
                                (mu1 - 3 * sigma_10 + 3 * sigma_31)
                            ) / 2 + 15 * delta_v1**3 * (
                                sigma_11 *
                                exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 / 2)
                                * sin(mu0 - 3 * sigma_30) +
                                (sigma_10 * exp(-3 * mu3 - sigma_00 / 2 +
                                                9 * sigma_33 / 2) *
                                 cos(mu0 - 3 * sigma_30) +
                                 (mu1 - 3 * sigma_31) *
                                 exp(-3 * mu3 - sigma_00 / 2 + 9 * sigma_33 /
                                     2) * sin(mu0 - 3 * sigma_30)) *
                                (mu1 - sigma_10 + 3 * sigma_31)
                            ) / 2 - 5 * delta_v1**2 * (
                                2 * sigma_11 *
                                (-2 * sigma_10 *
                                 exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                                 sin(2 * mu0 - 4 * sigma_30) +
                                 (mu1 - 2 * sigma_31) *
                                 exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                                 cos(2 * mu0 - 4 * sigma_30)) +
                                (sigma_11 *
                                 exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                                 cos(2 * mu0 - 4 * sigma_30) +
                                 (-2 * sigma_10 *
                                  exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                                  sin(2 * mu0 - 4 * sigma_30) +
                                  (mu1 - 2 * sigma_31) *
                                  exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                                  cos(2 * mu0 - 4 * sigma_30)) *
                                 (mu1 + 2 * sigma_10 + 2 * sigma_31)) *
                                (mu1 + 2 * sigma_10 + 2 * sigma_31)
                            ) + 5 * delta_v1**2 * (
                                2 * sigma_11 * (mu1 - 2 * sigma_31) *
                                exp(-2 * mu3 + 2 * sigma_33) +
                                (mu1 + 2 * sigma_31) *
                                (sigma_11 * exp(-2 * mu3 + 2 * sigma_33) +
                                 (mu1 - 2 * sigma_31) * (mu1 + 2 * sigma_31) *
                                 exp(-2 * mu3 + 2 * sigma_33))
                            ) + 5 * delta_v1 * (
                                3 * sigma_11 *
                                (sigma_11 * exp(-mu3 - sigma_00 / 2 + sigma_33
                                                / 2) * sin(mu0 - sigma_30) +
                                 (sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33
                                                 / 2) * cos(mu0 - sigma_30) +
                                  (mu1 - sigma_31) *
                                  exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                                  sin(mu0 - sigma_30)) *
                                 (mu1 - sigma_10 + sigma_31)) +
                                (2 * sigma_11 *
                                 (sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33
                                                 / 2) * cos(mu0 - sigma_30) +
                                  (mu1 - sigma_31) *
                                  exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                                  sin(mu0 - sigma_30)) +
                                 (sigma_11 * exp(-mu3 - sigma_00 / 2 + sigma_33
                                                 / 2) * sin(mu0 - sigma_30) +
                                  (sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33
                                                  / 2) * cos(mu0 - sigma_30) +
                                   (mu1 - sigma_31) *
                                   exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                                   sin(mu0 - sigma_30)) *
                                  (mu1 - sigma_10 + sigma_31)) *
                                 (mu1 - sigma_10 + sigma_31)) *
                                (mu1 - sigma_10 + sigma_31)) + mu1 * (
                                    mu1 *
                                    (2 * mu1 * sigma_11 + mu1 *
                                     (mu1**2 + sigma_11)) + 3 * sigma_11 *
                                    (mu1**2 + sigma_11)) + 4 * sigma_11 * (
                                        2 * mu1 * sigma_11 + mu1 *
                                        (mu1**2 + sigma_11))


def latex_0500():
    return r"""
-\frac{5}{8} \, {\Delta v_0}^{5} \cos\left(\mu_{0} - 5 \, \sigma_{30}\right) e^{\left(-5 \, \mu_{3} - \frac{1}{2} \,
\sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} - \frac{5}{4} \, {\Delta v_0}^{3} {\Delta v_1}^{2} \cos\left(\mu_{0} -
5 \, \sigma_{30}\right) e^{\left(-5 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} -
\frac{5}{8} \, {\Delta v_0} {\Delta v_1}^{4} \cos\left(\mu_{0} - 5 \, \sigma_{30}\right) e^{\left(-5 \, \mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} - \frac{5}{16} \, {\Delta v_0}^{5} \cos\left(3 \,
\mu_{0} - 15 \, \sigma_{30}\right) e^{\left(-5 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{25}{2} \,
\sigma_{33}\right)} + \frac{5}{8} \, {\Delta v_0}^{3} {\Delta v_1}^{2} \cos\left(3 \, \mu_{0} - 15 \, \sigma_{30}\right)
e^{\left(-5 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} + \frac{15}{16} \, {\Delta
v_0} {\Delta v_1}^{4} \cos\left(3 \, \mu_{0} - 15 \, \sigma_{30}\right) e^{\left(-5 \, \mu_{3} - \frac{9}{2} \,
\sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} - \frac{1}{16} \, {\Delta v_0}^{5} \cos\left(5 \, \mu_{0} - 25 \,
\sigma_{30}\right) e^{\left(-5 \, \mu_{3} - \frac{25}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} +
\frac{5}{8} \, {\Delta v_0}^{3} {\Delta v_1}^{2} \cos\left(5 \, \mu_{0} - 25 \, \sigma_{30}\right) e^{\left(-5 \,
\mu_{3} - \frac{25}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} - \frac{5}{16} \, {\Delta v_0} {\Delta
v_1}^{4} \cos\left(5 \, \mu_{0} - 25 \, \sigma_{30}\right) e^{\left(-5 \, \mu_{3} - \frac{25}{2} \, \sigma_{00} +
\frac{25}{2} \, \sigma_{33}\right)} + \frac{5}{16} \, {\Delta v_0}^{4} {\Delta v_1} e^{\left(-5 \, \mu_{3} -
\frac{25}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} \sin\left(5 \, \mu_{0} - 25 \, \sigma_{30}\right) -
\frac{5}{8} \, {\Delta v_0}^{2} {\Delta v_1}^{3} e^{\left(-5 \, \mu_{3} - \frac{25}{2} \, \sigma_{00} + \frac{25}{2} \,
\sigma_{33}\right)} \sin\left(5 \, \mu_{0} - 25 \, \sigma_{30}\right) + \frac{1}{16} \, {\Delta v_1}^{5} e^{\left(-5 \,
\mu_{3} - \frac{25}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} \sin\left(5 \, \mu_{0} - 25 \,
\sigma_{30}\right) + \frac{15}{16} \, {\Delta v_0}^{4} {\Delta v_1} e^{\left(-5 \, \mu_{3} - \frac{9}{2} \, \sigma_{00}
+ \frac{25}{2} \, \sigma_{33}\right)} \sin\left(3 \, \mu_{0} - 15 \, \sigma_{30}\right) + \frac{5}{8} \, {\Delta
v_0}^{2} {\Delta v_1}^{3} e^{\left(-5 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)}
\sin\left(3 \, \mu_{0} - 15 \, \sigma_{30}\right) - \frac{5}{16} \, {\Delta v_1}^{5} e^{\left(-5 \, \mu_{3} -
\frac{9}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} \sin\left(3 \, \mu_{0} - 15 \, \sigma_{30}\right) +
\frac{5}{8} \, {\Delta v_0}^{4} {\Delta v_1} e^{\left(-5 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{25}{2} \,
\sigma_{33}\right)} \sin\left(\mu_{0} - 5 \, \sigma_{30}\right) + \frac{5}{4} \, {\Delta v_0}^{2} {\Delta v_1}^{3}
e^{\left(-5 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{25}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - 5 \,
\sigma_{30}\right) + \frac{5}{8} \, {\Delta v_1}^{5} e^{\left(-5 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{25}{2}
\, \sigma_{33}\right)} \sin\left(\mu_{0} - 5 \, \sigma_{30}\right) + \frac{15}{8} \, {\Delta v_0}^{4} {\left(\mu_{1} - 4
\, \sigma_{31}\right)} e^{\left(-4 \, \mu_{3} + 8 \, \sigma_{33}\right)} + \frac{15}{4} \, {\Delta v_0}^{2} {\Delta
v_1}^{2} {\left(\mu_{1} - 4 \, \sigma_{31}\right)} e^{\left(-4 \, \mu_{3} + 8 \, \sigma_{33}\right)} + \frac{15}{8} \,
{\Delta v_1}^{4} {\left(\mu_{1} - 4 \, \sigma_{31}\right)} e^{\left(-4 \, \mu_{3} + 8 \, \sigma_{33}\right)} +
\frac{5}{2} \, {\left({\left(\mu_{1} - 4 \, \sigma_{31}\right)} \cos\left(2 \, \mu_{0} - 8 \, \sigma_{30}\right)
e^{\left(-4 \, \mu_{3} - 2 \, \sigma_{00} + 8 \, \sigma_{33}\right)} - 2 \, \sigma_{10} e^{\left(-4 \, \mu_{3} - 2 \,
\sigma_{00} + 8 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 8 \, \sigma_{30}\right)\right)} {\Delta v_0}^{4} +
\frac{5}{8} \, {\left({\left(\mu_{1} - 4 \, \sigma_{31}\right)} \cos\left(4 \, \mu_{0} - 16 \, \sigma_{30}\right)
e^{\left(-4 \, \mu_{3} - 8 \, \sigma_{00} + 8 \, \sigma_{33}\right)} - 4 \, \sigma_{10} e^{\left(-4 \, \mu_{3} - 8 \,
\sigma_{00} + 8 \, \sigma_{33}\right)} \sin\left(4 \, \mu_{0} - 16 \, \sigma_{30}\right)\right)} {\Delta v_0}^{4} - 5 \,
{\left(2 \, \sigma_{10} \cos\left(2 \, \mu_{0} - 8 \, \sigma_{30}\right) e^{\left(-4 \, \mu_{3} - 2 \, \sigma_{00} + 8
\, \sigma_{33}\right)} + {\left(\mu_{1} - 4 \, \sigma_{31}\right)} e^{\left(-4 \, \mu_{3} - 2 \, \sigma_{00} + 8 \,
\sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 8 \, \sigma_{30}\right)\right)} {\Delta v_0}^{3} {\Delta v_1} - \frac{5}{2}
\, {\left(4 \, \sigma_{10} \cos\left(4 \, \mu_{0} - 16 \, \sigma_{30}\right) e^{\left(-4 \, \mu_{3} - 8 \, \sigma_{00} +
8 \, \sigma_{33}\right)} + {\left(\mu_{1} - 4 \, \sigma_{31}\right)} e^{\left(-4 \, \mu_{3} - 8 \, \sigma_{00} + 8 \,
\sigma_{33}\right)} \sin\left(4 \, \mu_{0} - 16 \, \sigma_{30}\right)\right)} {\Delta v_0}^{3} {\Delta v_1} -
\frac{15}{4} \, {\left({\left(\mu_{1} - 4 \, \sigma_{31}\right)} \cos\left(4 \, \mu_{0} - 16 \, \sigma_{30}\right)
e^{\left(-4 \, \mu_{3} - 8 \, \sigma_{00} + 8 \, \sigma_{33}\right)} - 4 \, \sigma_{10} e^{\left(-4 \, \mu_{3} - 8 \,
\sigma_{00} + 8 \, \sigma_{33}\right)} \sin\left(4 \, \mu_{0} - 16 \, \sigma_{30}\right)\right)} {\Delta v_0}^{2}
{\Delta v_1}^{2} - 5 \, {\left(2 \, \sigma_{10} \cos\left(2 \, \mu_{0} - 8 \, \sigma_{30}\right) e^{\left(-4 \, \mu_{3}
- 2 \, \sigma_{00} + 8 \, \sigma_{33}\right)} + {\left(\mu_{1} - 4 \, \sigma_{31}\right)} e^{\left(-4 \, \mu_{3} - 2 \,
\sigma_{00} + 8 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 8 \, \sigma_{30}\right)\right)} {\Delta v_0} {\Delta
v_1}^{3} + \frac{5}{2} \, {\left(4 \, \sigma_{10} \cos\left(4 \, \mu_{0} - 16 \, \sigma_{30}\right) e^{\left(-4 \,
\mu_{3} - 8 \, \sigma_{00} + 8 \, \sigma_{33}\right)} + {\left(\mu_{1} - 4 \, \sigma_{31}\right)} e^{\left(-4 \, \mu_{3}
- 8 \, \sigma_{00} + 8 \, \sigma_{33}\right)} \sin\left(4 \, \mu_{0} - 16 \, \sigma_{30}\right)\right)} {\Delta v_0}
{\Delta v_1}^{3} - \frac{5}{2} \, {\left({\left(\mu_{1} - 4 \, \sigma_{31}\right)} \cos\left(2 \, \mu_{0} - 8 \,
\sigma_{30}\right) e^{\left(-4 \, \mu_{3} - 2 \, \sigma_{00} + 8 \, \sigma_{33}\right)} - 2 \, \sigma_{10} e^{\left(-4
\, \mu_{3} - 2 \, \sigma_{00} + 8 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 8 \, \sigma_{30}\right)\right)}
{\Delta v_1}^{4} + \frac{5}{8} \, {\left({\left(\mu_{1} - 4 \, \sigma_{31}\right)} \cos\left(4 \, \mu_{0} - 16 \,
\sigma_{30}\right) e^{\left(-4 \, \mu_{3} - 8 \, \sigma_{00} + 8 \, \sigma_{33}\right)} - 4 \, \sigma_{10} e^{\left(-4
\, \mu_{3} - 8 \, \sigma_{00} + 8 \, \sigma_{33}\right)} \sin\left(4 \, \mu_{0} - 16 \, \sigma_{30}\right)\right)}
{\Delta v_1}^{4} - \frac{15}{2} \, {\left(\sigma_{11} \cos\left(\mu_{0} - 3 \, \sigma_{30}\right) e^{\left(-3 \, \mu_{3}
- \frac{1}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} + {\left({\left(\mu_{1} - 3 \, \sigma_{31}\right)}
\cos\left(\mu_{0} - 3 \, \sigma_{30}\right) e^{\left(-3 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{9}{2} \,
\sigma_{33}\right)} - \sigma_{10} e^{\left(-3 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{9}{2} \,
\sigma_{33}\right)} \sin\left(\mu_{0} - 3 \, \sigma_{30}\right)\right)} {\left(\mu_{1} + \sigma_{10} + 3 \,
\sigma_{31}\right)}\right)} {\Delta v_0}^{3} - \frac{5}{2} \, {\left(\sigma_{11} \cos\left(3 \, \mu_{0} - 9 \,
\sigma_{30}\right) e^{\left(-3 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} +
{\left({\left(\mu_{1} - 3 \, \sigma_{31}\right)} \cos\left(3 \, \mu_{0} - 9 \, \sigma_{30}\right) e^{\left(-3 \, \mu_{3}
- \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} - 3 \, \sigma_{10} e^{\left(-3 \, \mu_{3} -
\frac{9}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} \sin\left(3 \, \mu_{0} - 9 \, \sigma_{30}\right)\right)}
{\left(\mu_{1} + 3 \, \sigma_{10} + 3 \, \sigma_{31}\right)}\right)} {\Delta v_0}^{3} + \frac{15}{2} \,
{\left(\sigma_{11} e^{\left(-3 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} \sin\left(3
\, \mu_{0} - 9 \, \sigma_{30}\right) + {\left(3 \, \sigma_{10} \cos\left(3 \, \mu_{0} - 9 \, \sigma_{30}\right)
e^{\left(-3 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} + {\left(\mu_{1} - 3 \,
\sigma_{31}\right)} e^{\left(-3 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} \sin\left(3
\, \mu_{0} - 9 \, \sigma_{30}\right)\right)} {\left(\mu_{1} - 3 \, \sigma_{10} + 3 \, \sigma_{31}\right)}\right)}
{\Delta v_0}^{2} {\Delta v_1} + \frac{15}{2} \, {\left(\sigma_{11} e^{\left(-3 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{9}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - 3 \, \sigma_{30}\right) + {\left(\sigma_{10} \cos\left(\mu_{0} -
3 \, \sigma_{30}\right) e^{\left(-3 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} +
{\left(\mu_{1} - 3 \, \sigma_{31}\right)} e^{\left(-3 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{9}{2} \,
\sigma_{33}\right)} \sin\left(\mu_{0} - 3 \, \sigma_{30}\right)\right)} {\left(\mu_{1} - \sigma_{10} + 3 \,
\sigma_{31}\right)}\right)} {\Delta v_0}^{2} {\Delta v_1} - \frac{15}{2} \, {\left(\sigma_{11} \cos\left(\mu_{0} - 3 \,
\sigma_{30}\right) e^{\left(-3 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} +
{\left({\left(\mu_{1} - 3 \, \sigma_{31}\right)} \cos\left(\mu_{0} - 3 \, \sigma_{30}\right) e^{\left(-3 \, \mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} - \sigma_{10} e^{\left(-3 \, \mu_{3} - \frac{1}{2} \,
\sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - 3 \, \sigma_{30}\right)\right)} {\left(\mu_{1} +
\sigma_{10} + 3 \, \sigma_{31}\right)}\right)} {\Delta v_0} {\Delta v_1}^{2} + \frac{15}{2} \, {\left(\sigma_{11}
\cos\left(3 \, \mu_{0} - 9 \, \sigma_{30}\right) e^{\left(-3 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \,
\sigma_{33}\right)} + {\left({\left(\mu_{1} - 3 \, \sigma_{31}\right)} \cos\left(3 \, \mu_{0} - 9 \, \sigma_{30}\right)
e^{\left(-3 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} - 3 \, \sigma_{10} e^{\left(-3
\, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} \sin\left(3 \, \mu_{0} - 9 \,
\sigma_{30}\right)\right)} {\left(\mu_{1} + 3 \, \sigma_{10} + 3 \, \sigma_{31}\right)}\right)} {\Delta v_0} {\Delta
v_1}^{2} - \frac{5}{2} \, {\left(\sigma_{11} e^{\left(-3 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \,
\sigma_{33}\right)} \sin\left(3 \, \mu_{0} - 9 \, \sigma_{30}\right) + {\left(3 \, \sigma_{10} \cos\left(3 \, \mu_{0} -
9 \, \sigma_{30}\right) e^{\left(-3 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} +
{\left(\mu_{1} - 3 \, \sigma_{31}\right)} e^{\left(-3 \, \mu_{3} - \frac{9}{2} \, \sigma_{00} + \frac{9}{2} \,
\sigma_{33}\right)} \sin\left(3 \, \mu_{0} - 9 \, \sigma_{30}\right)\right)} {\left(\mu_{1} - 3 \, \sigma_{10} + 3 \,
\sigma_{31}\right)}\right)} {\Delta v_1}^{3} + \frac{15}{2} \, {\left(\sigma_{11} e^{\left(-3 \, \mu_{3} - \frac{1}{2}
\, \sigma_{00} + \frac{9}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - 3 \, \sigma_{30}\right) + {\left(\sigma_{10}
\cos\left(\mu_{0} - 3 \, \sigma_{30}\right) e^{\left(-3 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{9}{2} \,
\sigma_{33}\right)} + {\left(\mu_{1} - 3 \, \sigma_{31}\right)} e^{\left(-3 \, \mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{9}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - 3 \, \sigma_{30}\right)\right)} {\left(\mu_{1} - \sigma_{10} + 3
\, \sigma_{31}\right)}\right)} {\Delta v_1}^{3} + 5 \, {\left(2 \, {\left(\mu_{1} - 2 \, \sigma_{31}\right)} \sigma_{11}
e^{\left(-2 \, \mu_{3} + 2 \, \sigma_{33}\right)} + {\left({\left(\mu_{1} + 2 \, \sigma_{31}\right)} {\left(\mu_{1} - 2
\, \sigma_{31}\right)} e^{\left(-2 \, \mu_{3} + 2 \, \sigma_{33}\right)} + \sigma_{11} e^{\left(-2 \, \mu_{3} + 2 \,
\sigma_{33}\right)}\right)} {\left(\mu_{1} + 2 \, \sigma_{31}\right)}\right)} {\Delta v_0}^{2} + 5 \,
{\left({\left(\sigma_{11} \cos\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right) e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2
\, \sigma_{33}\right)} + {\left({\left(\mu_{1} - 2 \, \sigma_{31}\right)} \cos\left(2 \, \mu_{0} - 4 \,
\sigma_{30}\right) e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} - 2 \, \sigma_{10} e^{\left(-2
\, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right)\right)}
{\left(\mu_{1} + 2 \, \sigma_{10} + 2 \, \sigma_{31}\right)}\right)} {\left(\mu_{1} + 2 \, \sigma_{10} + 2 \,
\sigma_{31}\right)} + 2 \, {\left({\left(\mu_{1} - 2 \, \sigma_{31}\right)} \cos\left(2 \, \mu_{0} - 4 \,
\sigma_{30}\right) e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} - 2 \, \sigma_{10} e^{\left(-2
\, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right)\right)}
\sigma_{11}\right)} {\Delta v_0}^{2} - 10 \, {\left({\left(\sigma_{11} e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \,
\sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right) + {\left(2 \, \sigma_{10} \cos\left(2 \, \mu_{0} -
4 \, \sigma_{30}\right) e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} + {\left(\mu_{1} - 2 \,
\sigma_{31}\right)} e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \,
\sigma_{30}\right)\right)} {\left(\mu_{1} - 2 \, \sigma_{10} + 2 \, \sigma_{31}\right)}\right)} {\left(\mu_{1} - 2 \,
\sigma_{10} + 2 \, \sigma_{31}\right)} + 2 \, {\left(2 \, \sigma_{10} \cos\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right)
e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} + {\left(\mu_{1} - 2 \, \sigma_{31}\right)}
e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \,
\sigma_{30}\right)\right)} \sigma_{11}\right)} {\Delta v_0} {\Delta v_1} + 5 \, {\left(2 \, {\left(\mu_{1} - 2 \,
\sigma_{31}\right)} \sigma_{11} e^{\left(-2 \, \mu_{3} + 2 \, \sigma_{33}\right)} + {\left({\left(\mu_{1} + 2 \,
\sigma_{31}\right)} {\left(\mu_{1} - 2 \, \sigma_{31}\right)} e^{\left(-2 \, \mu_{3} + 2 \, \sigma_{33}\right)} +
\sigma_{11} e^{\left(-2 \, \mu_{3} + 2 \, \sigma_{33}\right)}\right)} {\left(\mu_{1} + 2 \, \sigma_{31}\right)}\right)}
{\Delta v_1}^{2} - 5 \, {\left({\left(\sigma_{11} \cos\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right) e^{\left(-2 \,
\mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} + {\left({\left(\mu_{1} - 2 \, \sigma_{31}\right)} \cos\left(2 \,
\mu_{0} - 4 \, \sigma_{30}\right) e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} - 2 \,
\sigma_{10} e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \,
\sigma_{30}\right)\right)} {\left(\mu_{1} + 2 \, \sigma_{10} + 2 \, \sigma_{31}\right)}\right)} {\left(\mu_{1} + 2 \,
\sigma_{10} + 2 \, \sigma_{31}\right)} + 2 \, {\left({\left(\mu_{1} - 2 \, \sigma_{31}\right)} \cos\left(2 \, \mu_{0} -
4 \, \sigma_{30}\right) e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} - 2 \, \sigma_{10}
e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \,
\sigma_{30}\right)\right)} \sigma_{11}\right)} {\Delta v_1}^{2} - 5 \, {\left({\left({\left(\sigma_{11}
\cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \,
\sigma_{33}\right)} + {\left({\left(\mu_{1} - \sigma_{31}\right)} \cos\left(\mu_{0} - \sigma_{30}\right)
e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} - \sigma_{10} e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)}
{\left(\mu_{1} + \sigma_{10} + \sigma_{31}\right)}\right)} {\left(\mu_{1} + \sigma_{10} + \sigma_{31}\right)} + 2 \,
{\left({\left(\mu_{1} - \sigma_{31}\right)} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \,
\sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} - \sigma_{10} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)} \sigma_{11}\right)} {\left(\mu_{1} +
\sigma_{10} + \sigma_{31}\right)} + 3 \, {\left(\sigma_{11} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} + {\left({\left(\mu_{1} - \sigma_{31}\right)}
\cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \,
\sigma_{33}\right)} - \sigma_{10} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)}
\sin\left(\mu_{0} - \sigma_{30}\right)\right)} {\left(\mu_{1} + \sigma_{10} + \sigma_{31}\right)}\right)}
\sigma_{11}\right)} {\Delta v_0} + 5 \, {\left({\left({\left(\sigma_{11} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00}
+ \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right) + {\left(\sigma_{10} \cos\left(\mu_{0} -
\sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} + {\left(\mu_{1}
- \sigma_{31}\right)} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)}
\sin\left(\mu_{0} - \sigma_{30}\right)\right)} {\left(\mu_{1} - \sigma_{10} + \sigma_{31}\right)}\right)} {\left(\mu_{1}
- \sigma_{10} + \sigma_{31}\right)} + 2 \, {\left(\sigma_{10} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} + {\left(\mu_{1} - \sigma_{31}\right)} e^{\left(-\mu_{3}
- \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)}
\sigma_{11}\right)} {\left(\mu_{1} - \sigma_{10} + \sigma_{31}\right)} + 3 \, {\left(\sigma_{11} e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right) +
{\left(\sigma_{10} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2}
\, \sigma_{33}\right)} + {\left(\mu_{1} - \sigma_{31}\right)} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)} {\left(\mu_{1} - \sigma_{10} +
\sigma_{31}\right)}\right)} \sigma_{11}\right)} {\Delta v_1} + {\left({\left({\left(\mu_{1}^{2} + \sigma_{11}\right)}
\mu_{1} + 2 \, \mu_{1} \sigma_{11}\right)} \mu_{1} + 3 \, {\left(\mu_{1}^{2} + \sigma_{11}\right)} \sigma_{11}\right)}
\mu_{1} + 4 \, {\left({\left(\mu_{1}^{2} + \sigma_{11}\right)} \mu_{1} + 2 \, \mu_{1} \sigma_{11}\right)} \sigma_{11}
"""
