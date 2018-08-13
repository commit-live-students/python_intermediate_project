# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    d=np.genfromtxt(path,delimiter=',',skip_header=1)
    a=d[:,-6]
    return int(np.sum(a))
get_total_extras()

