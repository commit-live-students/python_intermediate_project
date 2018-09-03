# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path,dtype=np.float64):
    return np.genfromtxt(path,skip_header=1, delimiter=',', dtype=dtype)


