# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 2,0,0,1
# to recreate, then copy the file 'moment_2001.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_2001(delta_v, mu, sigma):
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

    return 2 * mu0 * sigma_30 + mu3 * (mu0**2 + sigma_00)


def latex_2001():
    return r"""
{\left(\mu_{0}^{2} + \sigma_{00}\right)} \mu_{3} + 2 \, \mu_{0} \sigma_{30}
"""
