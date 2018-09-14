# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    array = read_ipl_data_csv(path,'|S50')
    return sum(map(lambda x : int(x),array[0:,17:18].flatten()))
array = read_ipl_data_csv(path,'|S50')
su =0 
extras=array[0:,17:18].flatten()
extras = sum(map(lambda x : int(x),extras))
extras


