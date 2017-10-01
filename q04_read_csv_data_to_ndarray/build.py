
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))

import numpy as np

def read_csv_data_to_ndarray(path, dtype=np.float64):
    return np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=",")
