# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():
    array = read_ipl_data_csv(path, dtype = '|S100')
    extras_sum = np.array(array[:, 17], dtype = int).sum()
    return extras_sum





