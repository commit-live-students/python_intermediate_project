# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_matches_count():
    ipl_data=read_ipl_data_csv(path,'|S50')
    unique=np.unique(ipl_data[:,0])
    return len(unique)
    

