# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 2,1,0,0
# to recreate, then copy the file 'moment_2100.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_2100(delta_v, mu, sigma):
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
    sigma_30 = sigma[3, 0]
    sigma_33 = sigma[3, 3]

    return -delta_v0 * (
        sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
        cos(mu0 - sigma_30) +
        (-sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
         sin(mu0 - sigma_30) +
         (mu0 - sigma_30) * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
         cos(mu0 - sigma_30)) * (mu0 + sigma_00 + sigma_30)) + delta_v1 * (
             sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
             sin(mu0 - sigma_30) +
             (sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
              cos(mu0 - sigma_30) + (mu0 - sigma_30) *
              exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) * sin(mu0 - sigma_30)) *
             (mu0 - sigma_00 + sigma_30)) + 2 * mu0 * sigma_10 + mu1 * (
                 mu0**2 + sigma_00)


def latex_2100():
    return r"""
-{\left(\sigma_{00} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2}
\, \sigma_{33}\right)} + {\left({\left(\mu_{0} - \sigma_{30}\right)} \cos\left(\mu_{0} - \sigma_{30}\right)
e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} - \sigma_{00} e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)}
{\left(\mu_{0} + \sigma_{00} + \sigma_{30}\right)}\right)} {\Delta v_0} + {\left(\sigma_{00} e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right) +
{\left(\sigma_{00} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2}
\, \sigma_{33}\right)} + {\left(\mu_{0} - \sigma_{30}\right)} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)} {\left(\mu_{0} - \sigma_{00} +
\sigma_{30}\right)}\right)} {\Delta v_1} + {\left(\mu_{0}^{2} + \sigma_{00}\right)} \mu_{1} + 2 \, \mu_{0} \sigma_{10}
"""
