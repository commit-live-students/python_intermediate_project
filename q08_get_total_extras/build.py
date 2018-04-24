# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_matches_array =  read_ipl_data_csv(path,'|S20')
    extras_arr = ipl_matches_array[:,17].astype(np.float16)
    extras = extras_arr.sum()
    return extras

get_total_extras()
    


