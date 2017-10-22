# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = './data/ipl_matches_small.csv'

def read_ipl_data_csv(path,dtype):
    data = np.genfromtxt(path, dtype, skip_header=1, delimiter=",")
    return data
ipl_matches_array = read_ipl_data_csv(path,'|S20')
