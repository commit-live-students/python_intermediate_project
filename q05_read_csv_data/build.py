# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
dtype='|S50'
def read_ipl_data_csv(path, dtype):
    ipl_matches_array = np.genfromtxt(path, dtype, delimiter=";")

    return ipl_matches_array

read_ipl_data_csv(path, dtype)

# Enter code here
