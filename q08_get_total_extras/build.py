# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    arr = np.genfromtxt("data/ipl_matches_small.csv", delimiter = ',', dtype = '|S50', skip_header = 1)
    extras = arr[:,17:18].astype(np.int32)
    return np.sum(extras)
