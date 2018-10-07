# %load q05_read_csv_data/build.py
# Default imports
import numpy as np


# Enter code here
def read_ipl_data_csv(path,dtype):
    ipl_matches_array = np.genfromtxt(path,delimiter=',',dtype=dtype,skip_header=1)
    print(type(ipl_matches_array))
    return (ipl_matches_array)
read_ipl_data_csv('data/ipl_matches_small.csv', dtype='|S50')


