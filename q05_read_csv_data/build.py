# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
def read_ipl_data_csv(path,dtype='|S50'):
    ipl_matches_array=np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)
    #print(ipl_matches_array)
    return ipl_matches_array

# Enter code here


