# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 1,2,0,0
# to recreate, then copy the file 'moment_1200.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_1200(delta_v, mu, sigma):
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

    return delta_v0**2 * (
        mu0 - 2 * sigma_30
    ) * exp(-2 * mu3 + 2 * sigma_33) / 2 + delta_v0**2 * (
        -2 * sigma_00 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
        sin(2 * mu0 - 4 * sigma_30) +
        (mu0 - 2 * sigma_30) * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
        cos(2 * mu0 - 4 * sigma_30)) / 2 - delta_v0 * delta_v1 * (
            2 * sigma_00 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
            cos(2 * mu0 - 4 * sigma_30) +
            (mu0 - 2 * sigma_30) * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33)
            * sin(2 * mu0 - 4 * sigma_30)) - 2 * delta_v0 * (
                sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                cos(mu0 - sigma_30) +
                (-sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                 sin(mu0 - sigma_30) +
                 (mu0 - sigma_30) * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                 cos(mu0 - sigma_30)) *
                (mu1 + sigma_10 + sigma_31)) + delta_v1**2 * (
                    mu0 - 2 * sigma_30
                ) * exp(-2 * mu3 + 2 * sigma_33) / 2 - delta_v1**2 * (
                    -2 * sigma_00 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33)
                    * sin(2 * mu0 - 4 * sigma_30) + (mu0 - 2 * sigma_30) *
                    exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) *
                    cos(2 * mu0 - 4 * sigma_30)
                ) / 2 + 2 * delta_v1 * (
                    sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                    sin(mu0 - sigma_30) +
                    (sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                     cos(mu0 - sigma_30) +
                     (mu0 - sigma_30) * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2)
                     * sin(mu0 - sigma_30)) * (mu1 - sigma_10 + sigma_31)
                ) + mu0 * sigma_11 + mu1 * sigma_10 + mu1 * (mu0 * mu1 +
                                                             sigma_10)


def latex_1200():
    return r"""
\frac{1}{2} \, {\Delta v_0}^{2} {\left(\mu_{0} - 2 \, \sigma_{30}\right)} e^{\left(-2 \, \mu_{3} + 2 \,
\sigma_{33}\right)} + \frac{1}{2} \, {\Delta v_1}^{2} {\left(\mu_{0} - 2 \, \sigma_{30}\right)} e^{\left(-2 \, \mu_{3} +
2 \, \sigma_{33}\right)} + \frac{1}{2} \, {\left({\left(\mu_{0} - 2 \, \sigma_{30}\right)} \cos\left(2 \, \mu_{0} - 4 \,
\sigma_{30}\right) e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} - 2 \, \sigma_{00} e^{\left(-2
\, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right)\right)}
{\Delta v_0}^{2} - {\left(2 \, \sigma_{00} \cos\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right) e^{\left(-2 \, \mu_{3} - 2
\, \sigma_{00} + 2 \, \sigma_{33}\right)} + {\left(\mu_{0} - 2 \, \sigma_{30}\right)} e^{\left(-2 \, \mu_{3} - 2 \,
\sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right)\right)} {\Delta v_0} {\Delta
v_1} - \frac{1}{2} \, {\left({\left(\mu_{0} - 2 \, \sigma_{30}\right)} \cos\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right)
e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} - 2 \, \sigma_{00} e^{\left(-2 \, \mu_{3} - 2 \,
\sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right)\right)} {\Delta v_1}^{2} - 2 \,
{\left(\sigma_{10} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2}
\, \sigma_{33}\right)} + {\left({\left(\mu_{0} - \sigma_{30}\right)} \cos\left(\mu_{0} - \sigma_{30}\right)
e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} - \sigma_{00} e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)}
{\left(\mu_{1} + \sigma_{10} + \sigma_{31}\right)}\right)} {\Delta v_0} + 2 \, {\left(\sigma_{10} e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right) +
{\left(\sigma_{00} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2}
\, \sigma_{33}\right)} + {\left(\mu_{0} - \sigma_{30}\right)} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)} {\left(\mu_{1} - \sigma_{10} +
\sigma_{31}\right)}\right)} {\Delta v_1} + {\left(\mu_{0} \mu_{1} + \sigma_{10}\right)} \mu_{1} + \mu_{1} \sigma_{10} +
\mu_{0} \sigma_{11}
"""
