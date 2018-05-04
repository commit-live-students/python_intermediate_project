# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
def get_total_extras():
    match_data=read_ipl_data_csv(path,dtype='|S20')
    extras=match_data[:,17].astype(np.int16)
    return extras.sum()

# Enter Code Here
match_data=read_ipl_data_csv(path,dtype='|S20')
extras=match_data[:,17].astype(np.int16)
match_data[:,17]
extras
extras.sum()


