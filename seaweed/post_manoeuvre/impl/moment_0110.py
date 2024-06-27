# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 0,1,1,0
# to recreate, then copy the file 'moment_0110.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_0110(delta_v, mu, sigma):
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
    mu2 = mu[2]
    mu3 = mu[3]
    sigma_00 = sigma[0, 0]
    sigma_10 = sigma[1, 0]
    sigma_20 = sigma[2, 0]
    sigma_21 = sigma[2, 1]
    sigma_30 = sigma[3, 0]
    sigma_31 = sigma[3, 1]
    sigma_32 = sigma[3, 2]
    sigma_33 = sigma[3, 3]

    return delta_v0**2 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) * sin(
        2 * mu0 - 4 * sigma_30) / 2 + delta_v0 * delta_v1 * exp(
            -2 * mu3 - 2 * sigma_00 + 2 * sigma_33
        ) * cos(2 * mu0 - 4 * sigma_30) - delta_v0 * (
            sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
            cos(mu0 - sigma_30) + (mu1 - sigma_31) *
            exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) * sin(mu0 - sigma_30)
        ) - delta_v0 * (
            -sigma_20 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
            sin(mu0 - sigma_30) +
            (mu2 - sigma_32) * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
            cos(mu0 - sigma_30)
        ) - delta_v1**2 * exp(-2 * mu3 - 2 * sigma_00 + 2 * sigma_33) * sin(
            2 * mu0 - 4 * sigma_30) / 2 - delta_v1 * (
                -sigma_10 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                sin(mu0 - sigma_30) +
                (mu1 - sigma_31) * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                cos(mu0 - sigma_30)) + delta_v1 * (
                    sigma_20 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
                    cos(mu0 - sigma_30) +
                    (mu2 - sigma_32) * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2)
                    * sin(mu0 - sigma_30)) + mu1 * mu2 + sigma_21


def latex_0110():
    return r"""
{\Delta v_0} {\Delta v_1} \cos\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right) e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2
\, \sigma_{33}\right)} + \frac{1}{2} \, {\Delta v_0}^{2} e^{\left(-2 \, \mu_{3} - 2 \, \sigma_{00} + 2 \,
\sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right) - \frac{1}{2} \, {\Delta v_1}^{2} e^{\left(-2 \,
\mu_{3} - 2 \, \sigma_{00} + 2 \, \sigma_{33}\right)} \sin\left(2 \, \mu_{0} - 4 \, \sigma_{30}\right) -
{\left({\left(\mu_{2} - \sigma_{32}\right)} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \,
\sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} - \sigma_{20} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)} {\Delta v_0} - {\left(\sigma_{10}
\cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \,
\sigma_{33}\right)} + {\left(\mu_{1} - \sigma_{31}\right)} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2}
\, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)} {\Delta v_0} - {\left({\left(\mu_{1} -
\sigma_{31}\right)} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2}
\, \sigma_{33}\right)} - \sigma_{10} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)}
\sin\left(\mu_{0} - \sigma_{30}\right)\right)} {\Delta v_1} + {\left(\sigma_{20} \cos\left(\mu_{0} - \sigma_{30}\right)
e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} + {\left(\mu_{2} -
\sigma_{32}\right)} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)}
\sin\left(\mu_{0} - \sigma_{30}\right)\right)} {\Delta v_1} + \mu_{1} \mu_{2} + \sigma_{21}
"""
