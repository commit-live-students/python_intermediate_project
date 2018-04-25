# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
array=np.array(0)

def get_total_extras():
    data=read_ipl_data_csv(path,'int32')
    x=np.array(data[0:,-6])
    
    
    return(np.sum(x))
get_total_extras()
# Enter Code Here

