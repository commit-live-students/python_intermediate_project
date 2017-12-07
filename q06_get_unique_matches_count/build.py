# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

import numpy as np
# Enter Code Here
def get_unique_matches_count():
    #ipl_matches_arraay = np.loadtxt('data/ipl_matches_small.csv')
    data1 =  np.genfromtxt(path, dtype = 'str', delimiter = ",", skip_header = 1)
    data1 = data1[:, :1]
    ipl_matches_array = np.unique(data1).shape[0]
    #print type(ipl_matches_array)
    return ipl_matches_array

print get_unique_matches_count()
