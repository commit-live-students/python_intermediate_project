# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np


path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    extras = 0
    array = read_ipl_data_csv('data/ipl_matches_small.csv', dtype = '|S50')
    runs = np.array(array[:,-6], dtype = int).sum()
    extras = (runs)
    print (extras)
    return extras
get_total_extras()


