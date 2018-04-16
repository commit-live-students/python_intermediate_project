# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
# Enter code here
path = './data/ipl_matches_small.csv'
def read_ipl_data_csv(path,dtype='|S50'):
    ipl_matches_array = np.genfromtxt(path,dtype=dtype,skip_header=1,delimiter=',')
    #print(type(ipl_matches_array))
    return ipl_matches_array

ipl_matches_array = read_ipl_data_csv(path)

