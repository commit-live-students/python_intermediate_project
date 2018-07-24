# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_unique_matches_count():
    
    ipl_matches_array=np.genfromtxt(path,dtype='|S50',delimiter=',',skip_header=1)
    matches_code=ipl_matches_array[:,0].astype(np.int64)
    unique_count=np.unique(matches_code).size
    return unique_count

get_unique_matches_count()



