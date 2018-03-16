# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    data = np.genfromtxt(path, dtype='str',delimiter = ",", skip_header = 1)
    data1 = data[:,:1]
    ipl_matches_array = np.unique(data1).shape[0]
    return ipl_matches_array
