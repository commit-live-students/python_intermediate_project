
# Default imports
import numpy as np

def read_ipl_data_csv(path, dtype):

    return np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=',')

