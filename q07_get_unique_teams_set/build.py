# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    varfile=np.genfromtxt(path,delimiter=',',skip_header=1,dtype='|S50')
    var1=np.unique(varfile[:,3])
    var2=np.unique(varfile[:,4])
    return set(np.union1d(var1,var2))
    
get_unique_teams_set()


