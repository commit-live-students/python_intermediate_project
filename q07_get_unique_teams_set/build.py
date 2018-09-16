# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

import numpy as np
# Enter Code Here
def get_unique_teams_set():
    
    ipl_matches_array=np.genfromtxt(path, dtype='|S50',delimiter=',',skip_header=1)
        
    u1=list(np.unique(ipl_matches_array[:,3]))
    u2=list(np.unique(ipl_matches_array[:,4]))
        
    
    
    u=set(u1+u2)
    
        
    return u



