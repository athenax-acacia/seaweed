# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 1,0,0,4
# to recreate, then copy the file 'moment_1004.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_1004(delta_v, mu, sigma):
    delta_v = np.atleast_1d(delta_v)
    mu = np.atleast_1d(mu)
    sigma = np.atleast_2d(sigma)

    assert delta_v.shape == (2, )
    assert mu.shape == (4, )
    assert sigma.shape == (4, 4)

    mu0 = mu[0]
    mu3 = mu[3]
    sigma_30 = sigma[3, 0]
    sigma_33 = sigma[3, 3]

    return mu3 * (mu3 * (mu0 * sigma_33 + mu3 * sigma_30 + mu3 *
                         (mu0 * mu3 + sigma_30)) + sigma_30 *
                  (mu3**2 + sigma_33) + 2 * sigma_33 *
                  (mu0 * mu3 + sigma_30)) + sigma_30 * (
                      2 * mu3 * sigma_33 + mu3 *
                      (mu3**2 + sigma_33)) + 3 * sigma_33 * (
                          mu0 * sigma_33 + mu3 * sigma_30 + mu3 *
                          (mu0 * mu3 + sigma_30))


def latex_1004():
    return r"""
{\left({\left({\left(\mu_{0} \mu_{3} + \sigma_{30}\right)} \mu_{3} + \mu_{3} \sigma_{30} + \mu_{0} \sigma_{33}\right)}
\mu_{3} + {\left(\mu_{3}^{2} + \sigma_{33}\right)} \sigma_{30} + 2 \, {\left(\mu_{0} \mu_{3} + \sigma_{30}\right)}
\sigma_{33}\right)} \mu_{3} + {\left({\left(\mu_{3}^{2} + \sigma_{33}\right)} \mu_{3} + 2 \, \mu_{3} \sigma_{33}\right)}
\sigma_{30} + 3 \, {\left({\left(\mu_{0} \mu_{3} + \sigma_{30}\right)} \mu_{3} + \mu_{3} \sigma_{30} + \mu_{0}
\sigma_{33}\right)} \sigma_{33}
"""
