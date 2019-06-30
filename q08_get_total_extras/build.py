# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
dtype='|S50'
# Enter Code Here

def get_total_extras():
    ipl_matches_array=read_ipl_data_csv(path,dtype)
    extras_array=ipl_matches_array[:,17].astype(np.int32)
    
    return np.sum(extras_array)

get_total_extras()


