# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 3,0,0,2
# to recreate, then copy the file 'moment_3002.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_3002(delta_v, mu, sigma):
    delta_v = np.atleast_1d(delta_v)
    mu = np.atleast_1d(mu)
    sigma = np.atleast_2d(sigma)

    assert delta_v.shape == (2, )
    assert mu.shape == (4, )
    assert sigma.shape == (4, 4)

    mu0 = mu[0]
    mu3 = mu[3]
    sigma_00 = sigma[0, 0]
    sigma_30 = sigma[3, 0]
    sigma_33 = sigma[3, 3]

    return mu3 * (mu3 * (2 * mu0 * sigma_00 + mu0 *
                         (mu0**2 + sigma_00)) + 3 * sigma_30 *
                  (mu0**2 + sigma_00)) + 3 * sigma_30 * (
                      2 * mu0 * sigma_30 + mu3 *
                      (mu0**2 + sigma_00)) + sigma_33 * (2 * mu0 * sigma_00 +
                                                         mu0 *
                                                         (mu0**2 + sigma_00))


def latex_3002():
    return r"""
{\left({\left({\left(\mu_{0}^{2} + \sigma_{00}\right)} \mu_{0} + 2 \, \mu_{0} \sigma_{00}\right)} \mu_{3} + 3 \,
{\left(\mu_{0}^{2} + \sigma_{00}\right)} \sigma_{30}\right)} \mu_{3} + 3 \, {\left({\left(\mu_{0}^{2} +
\sigma_{00}\right)} \mu_{3} + 2 \, \mu_{0} \sigma_{30}\right)} \sigma_{30} + {\left({\left(\mu_{0}^{2} +
\sigma_{00}\right)} \mu_{0} + 2 \, \mu_{0} \sigma_{00}\right)} \sigma_{33}
"""
