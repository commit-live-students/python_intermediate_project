# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here

def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv', dtype='|S50')
    a= np.unique(ar=ipl_matches_array[:,3])
    c= np.unique(ar=ipl_matches_array[:,4])
    return_set=set(np.union1d(a,c))
    return return_set
