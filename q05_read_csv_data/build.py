# Default imports
import numpy as np

path = 'data/ipl_matches_small.csv'
# Enter code here
def read_ipl_data_csv(path, dtype):
    input_dtype = '|S50'

    ipl_matches_array =np.genfromtxt (path, delimiter=",", skip_header=1)

    l =  list(ipl_matches_array)
    ipl_matches_array = np.array(l, dtype=dtype)
    return ipl_matches_array
