# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 1,0,0,1
# to recreate, then copy the file 'moment_1001.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_1001(delta_v, mu, sigma):
    delta_v = np.atleast_1d(delta_v)
    mu = np.atleast_1d(mu)
    sigma = np.atleast_2d(sigma)

    assert delta_v.shape == (2, )
    assert mu.shape == (4, )
    assert sigma.shape == (4, 4)

    mu0 = mu[0]
    mu3 = mu[3]
    sigma_30 = sigma[3, 0]

    return mu0 * mu3 + sigma_30


def latex_1001():
    return r"""
\mu_{0} \mu_{3} + \sigma_{30}
"""
