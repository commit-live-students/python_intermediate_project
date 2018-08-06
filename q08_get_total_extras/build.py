# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
extras = 0
# Enter Code Here
def get_total_extras():
    ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', delimiter=',', skip_header=1)
    extras_col = ipl_matches_array[:, 17]
    runs = np.sum(extras_col, axis=0)
    return runs


