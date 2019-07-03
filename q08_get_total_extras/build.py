# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    ipl=read_ipl_data_csv(path,dtype=int)
    extras = [x[17] for x in ipl[:]]
    return sum(extras)
        
    




# Enter Code Here
get_total_extras()


