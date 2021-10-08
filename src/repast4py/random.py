# Copyright 2021, UChicago Argonne, LLC
# All Rights Reserved
# Software Name: repast4py
# By: Argonne National Laboratory
# License: BSD-3 - https://github.com/Repast/repast4py/blob/master/LICENSE.txt

"""Random numbers for repast4py
"""

import numpy as np
import time
import torch

default_rng: np.random.Generator = None
"""numpy.random.Generator: default random generator created using init
"""

seed: int = None
"""Current random seed"""


def init(rng_seed: int=None):
    """Initializes the default random number generator using the specified seed

    Args:
        seed: the random number seed
    """
    global default_rng, seed
    seed = rng_seed
    torch.manual_seed(rng_seed)
    default_rng = np.random.default_rng(rng_seed)


init(int(time.time()))
