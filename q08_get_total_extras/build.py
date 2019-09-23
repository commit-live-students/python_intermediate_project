# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
dtype = np.int
def get_total_extras():
    var = read_ipl_data_csv(path, dtype)
    return sum(var[:,17])
