# Default imports
import numpy as np



def read_ipl_data_csv(filepath,dtype):
    ipl_matches_array=np.genfromtxt(filepath,dtype=dtype,delimiter=',',skip_header=1)
    return ipl_matches_array
read_ipl_data_csv('data/ipl_matches_small.csv', dtype='|S50')
