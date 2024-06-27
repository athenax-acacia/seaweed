# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 3,0,1,0
# to recreate, then copy the file 'moment_3010.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_3010(delta_v, mu, sigma):
    delta_v = np.atleast_1d(delta_v)
    mu = np.atleast_1d(mu)
    sigma = np.atleast_2d(sigma)

    assert delta_v.shape == (2, )
    assert mu.shape == (4, )
    assert sigma.shape == (4, 4)

    delta_v0 = delta_v[0]
    delta_v1 = delta_v[1]
    mu0 = mu[0]
    mu2 = mu[2]
    mu3 = mu[3]
    sigma_00 = sigma[0, 0]
    sigma_20 = sigma[2, 0]
    sigma_30 = sigma[3, 0]
    sigma_33 = sigma[3, 3]

    return -delta_v0 * (
        2 * sigma_00 *
        (sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
         cos(mu0 - sigma_30) + (mu0 - sigma_30) *
         exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) * sin(mu0 - sigma_30)) +
        (sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
         sin(mu0 - sigma_30) +
         (sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
          cos(mu0 - sigma_30) + (mu0 - sigma_30) *
          exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) * sin(mu0 - sigma_30)) *
         (mu0 - sigma_00 + sigma_30)) *
        (mu0 - sigma_00 + sigma_30)) - delta_v1 * (
            2 * sigma_00 *
            (-sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
             sin(mu0 - sigma_30) + (mu0 - sigma_30) *
             exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) * cos(mu0 - sigma_30)) +
            (sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
             cos(mu0 - sigma_30) +
             (-sigma_00 * exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) *
              sin(mu0 - sigma_30) + (mu0 - sigma_30) *
              exp(-mu3 - sigma_00 / 2 + sigma_33 / 2) * cos(mu0 - sigma_30)) *
             (mu0 + sigma_00 + sigma_30)) *
            (mu0 + sigma_00 + sigma_30)) + mu2 * (
                2 * mu0 * sigma_00 + mu0 *
                (mu0**2 + sigma_00)) + 3 * sigma_20 * (mu0**2 + sigma_00)


def latex_3010():
    return r"""
-{\left({\left(\sigma_{00} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)}
\sin\left(\mu_{0} - \sigma_{30}\right) + {\left(\sigma_{00} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} + {\left(\mu_{0} - \sigma_{30}\right)} e^{\left(-\mu_{3}
- \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)}
{\left(\mu_{0} - \sigma_{00} + \sigma_{30}\right)}\right)} {\left(\mu_{0} - \sigma_{00} + \sigma_{30}\right)} + 2 \,
{\left(\sigma_{00} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2}
\, \sigma_{33}\right)} + {\left(\mu_{0} - \sigma_{30}\right)} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)} \sigma_{00}\right)} {\Delta v_0} -
{\left({\left(\sigma_{00} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{1}{2} \, \sigma_{33}\right)} + {\left({\left(\mu_{0} - \sigma_{30}\right)} \cos\left(\mu_{0} - \sigma_{30}\right)
e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} - \sigma_{00} e^{\left(-\mu_{3} -
\frac{1}{2} \, \sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)}
{\left(\mu_{0} + \sigma_{00} + \sigma_{30}\right)}\right)} {\left(\mu_{0} + \sigma_{00} + \sigma_{30}\right)} + 2 \,
{\left({\left(\mu_{0} - \sigma_{30}\right)} \cos\left(\mu_{0} - \sigma_{30}\right) e^{\left(-\mu_{3} - \frac{1}{2} \,
\sigma_{00} + \frac{1}{2} \, \sigma_{33}\right)} - \sigma_{00} e^{\left(-\mu_{3} - \frac{1}{2} \, \sigma_{00} +
\frac{1}{2} \, \sigma_{33}\right)} \sin\left(\mu_{0} - \sigma_{30}\right)\right)} \sigma_{00}\right)} {\Delta v_1} +
{\left({\left(\mu_{0}^{2} + \sigma_{00}\right)} \mu_{0} + 2 \, \mu_{0} \sigma_{00}\right)} \mu_{2} + 3 \,
{\left(\mu_{0}^{2} + \sigma_{00}\right)} \sigma_{20}
"""
