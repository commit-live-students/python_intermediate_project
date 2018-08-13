# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array=np.genfromtxt(path,dtype='|S50',skip_header=1,delimiter=',')
    x=ipl_matches_array[:,3]
    y=ipl_matches_array[:,4]
    z=(list(x)+list(y))
    return set(z)
get_unique_teams_set()


