# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    
    matches = np.genfromtxt(path, skip_header = 1, delimiter = ',')
    
    #np.set_printoptions(threshold = np.nan)
    
    ipl_matches_array = len(set(matches[:,0]))
    
    return ipl_matches_array
    
get_unique_matches_count()
    
    


