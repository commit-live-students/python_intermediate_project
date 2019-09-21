# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    
    def read_ipl_data_csv():
        ipl_matches_array=np.genfromtxt(path, dtype='|S50', skip_header=1, delimiter=',')
        return (ipl_matches_array)
        
    ipl_matches_array=read_ipl_data_csv()
    t1=set(ipl_matches_array[:,3])
    t2=set(ipl_matches_array[:,4])
    return (t1.union(t2))

    
get_unique_teams_set()


