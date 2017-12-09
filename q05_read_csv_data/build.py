# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(file_path, dtype):
    return np.genfromtxt(file_path, delimiter=',', dtype=dtype, skip_header=1)
