# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path, dtype='float64'):
    with open(path) as csv:
        ipl_matches_array = np.genfromtxt(csv, dtype=dtype, delimiter=',', skip_header=1)
    return ipl_matches_array
