# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here

def get_unique_matches_count ():
    ipl_matches_data = np.genfromtxt(path, dtype='|S50', delimiter=',')
    unique_matches = np.unique(ipl_matches_data[:, 0])
    ipl_matches_array = len(unique_matches)-1
    return ipl_matches_array
