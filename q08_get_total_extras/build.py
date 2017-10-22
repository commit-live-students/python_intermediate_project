# %load q08_get_total_extras/build.py
# Default Imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_total_extras():
    ipl_matches_array = read_ipl_data_csv(path,dtype = 'int')
    extras = np.sum(ipl_matches_array[:,17],axis=0)
    return extras
