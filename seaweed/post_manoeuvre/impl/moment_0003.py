# This is a generated file. Do not edit. Run:
#     sage post-manoeuvre-moments.sage --output-folder <some/temp/dir> -v --order 0,0,0,3
# to recreate, then copy the file 'moment_0003.py' on top of this one.

import numpy as np

sin = np.sin
cos = np.cos
exp = np.exp


def moment_0003(delta_v, mu, sigma):
    delta_v = np.atleast_1d(delta_v)
    mu = np.atleast_1d(mu)
    sigma = np.atleast_2d(sigma)

    assert delta_v.shape == (2, )
    assert mu.shape == (4, )
    assert sigma.shape == (4, 4)

    mu3 = mu[3]
    sigma_33 = sigma[3, 3]

    return 2 * mu3 * sigma_33 + mu3 * (mu3**2 + sigma_33)


def latex_0003():
    return r"""
{\left(\mu_{3}^{2} + \sigma_{33}\right)} \mu_{3} + 2 \, \mu_{3} \sigma_{33}
"""
