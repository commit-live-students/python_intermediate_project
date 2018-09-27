# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = './data/ipl_matches_small.csv'
dtype ='|S50'
def get_total_extras():
    ipl_matches=read_ipl_data_csv(path,dtype)
    extras=ipl_matches[:,17].astype(np.int64)
    return extras.sum()
# Enter Code Here



