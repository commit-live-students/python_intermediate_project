
# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

import numpy as np


def read_ipl_data_csv(path, dtype):

    return np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=",")
