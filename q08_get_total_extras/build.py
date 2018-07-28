# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np


# Enter Code Here

def get_total_extras():
    path = 'data/ipl_matches_small.csv'
    dataset = np.genfromtxt(path, dtype='|S20', skip_header = 1,delimiter =',')
    variable = dataset[:,17].astype(np.int16).sum()
    return variable

get_total_extras()



