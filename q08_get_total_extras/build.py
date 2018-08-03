# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
dtype = 'S100'

# Enter Code Here
def get_total_extras():
    extra_score = 0
    ipl_data = read_ipl_data_csv(path, dtype)
    extras_list = ipl_data[:,17]
    for extra_run in extras_list:
        extra_score = extra_score + int(extra_run)
    return extra_score
    
get_total_extras()

