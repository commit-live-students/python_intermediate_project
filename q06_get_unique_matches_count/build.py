# Default imports
import numpy as np
from numpy import genfromtxt
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    data = np.genfromtxt(path,dtype='|S50',skip_header = 1,delimiter =',')
    ipl_matches_array = np.unique(data[:,0])
    return len(ipl_matches_array)
