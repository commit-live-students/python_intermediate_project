# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv as ipld
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_matches_array1 = np.genfromtxt(path, dtype='str', delimiter=",", skip_header=1)
    new_array = ipl_matches_array1[:,:1]
    ipl_matches_array = np.unique(new_array).shape[0]
    return ipl_matches_array

print get_unique_matches_count()
