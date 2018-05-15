# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():
    extra=0
    data=read_ipl_data_csv(path,'|S50')
    
    for i in range(0,data.shape[0]):
        extra += int(data[i][17])
    return extra
    


