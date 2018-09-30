# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    
    ipl_df = read_ipl_data_csv(path,dtype = 'S50')
    ipl_new = ipl_df[:,[3,4]]
    ipl_unique = set(np.unique(ipl_new))
    return ipl_unique

# ipl_df


