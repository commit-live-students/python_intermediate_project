# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    data = read_ipl_data_csv(path,'int64')
    extras = data[:,17]
    return int(np.sum(extras))

print(get_total_extras())





