# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import pandas as pd

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    extras  = pd.DataFrame(read_ipl_data_csv('data/ipl_matches_small.csv','|S100'))[17]
    return np.sum(extras.astype(np.int))



