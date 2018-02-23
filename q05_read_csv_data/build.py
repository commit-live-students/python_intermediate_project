# Default imports
import numpy as np
def read_ipl_data_csv(path,dtype):
    ipl_matches_array = np.genfromtxt(path,skip_header=1,delimiter=',',dtype='|S50')
    return ipl_matches_array
# Enter code here
