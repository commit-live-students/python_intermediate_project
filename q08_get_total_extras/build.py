# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# funtion to calculate extras
def get_total_extras():
    extras = sum(read_ipl_data_csv(path,'int32')[:,-6])
    return extras

get_total_extras()


