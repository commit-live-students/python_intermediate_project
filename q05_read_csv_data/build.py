# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path, dtype):

    return np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=',')

