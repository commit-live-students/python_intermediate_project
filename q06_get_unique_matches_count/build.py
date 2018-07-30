# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    array = read_ipl_data_csv('data/ipl_matches_small.csv', dtype='|S50')
    
    print(len(set(array[:,0])))
    return(len(set(array[:,0])))

get_unique_matches_count()
    


