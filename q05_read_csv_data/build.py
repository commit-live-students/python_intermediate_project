# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = './data/ipl_matches_small.csv'
def read_ipl_data_csv(path,dtype=np.float64):
    ipl_matches_array = np.genfromtxt(path,dtype = np.float64)

    return np.array(ipl_matches_array, dtype = '|S50')
read_ipl_data_csv(path)


