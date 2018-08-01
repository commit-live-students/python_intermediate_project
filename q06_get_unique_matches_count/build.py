# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_matches_count():
    ipl_data = read_ipl_data_csv(path, np.float64)
    a = ipl_data.view(np.float64).reshape(len(ipl_data), -1)
    return len(np.unique(a[:, 0]))

get_unique_matches_count()




