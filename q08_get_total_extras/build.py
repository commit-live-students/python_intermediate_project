# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import pandas as pd
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    data = np.genfromtxt(path, delimiter=',', dtype=np.int64,skip_header=1)
    total_extras = np.sum(data[:,17])
    return total_extras


get_total_extras()
