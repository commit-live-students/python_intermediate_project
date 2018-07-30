# %load q05_read_csv_data/build.py


# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

def read_ipl_data_csv(path, dtype=np.float64):
    ipl_matches_array = np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=',')
    return ipl_matches_array

read_ipl_data_csv(path)
 




