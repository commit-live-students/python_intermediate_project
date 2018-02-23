# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
dtype = '|S20'
def read_ipl_data_csv(path, dtype):
    ipl_matches_array = np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=",")
    return ipl_matches_array

def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path, dtype)
    return len(set(ipl_matches_array[:,0]))

print get_unique_matches_count()
