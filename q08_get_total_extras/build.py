# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
# Enter Code Here
path = 'data/ipl_matches_small.csv'
def get_total_extras():
    m = read_ipl_data_csv(path,'|S50')
    extras = sum(m[0:,17].astype(np.int16))
    
    return extras

