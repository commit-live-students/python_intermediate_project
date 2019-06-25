# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = './data/ipl_matches_small.csv'

# load array from csv file
def read_ipl_data_csv(path,dtype):
    ipl_matches_array = np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)
    return ipl_matches_array

read_ipl_data_csv(path,'|S50')
print(read_ipl_data_csv(path,'|S50'))



