# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

def read_ipl_data_csv(path , dtype):
    ipl_matches_array = np.genfromtxt(path , delimiter = ',',dtype = dtype)
    return ipl_matches_array


