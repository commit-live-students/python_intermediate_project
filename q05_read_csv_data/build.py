# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

def read_ipl_data_csv(path, dtype):
    arr = np.genfromtxt(path, delimiter=',', dtype = dtype, skip_header=1)
    return arr


# Enter code here


