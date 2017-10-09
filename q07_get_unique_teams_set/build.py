# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
def get_unique_teams_set():
    ipl_matches_array = np.genfromtxt(path,dtype='|S50',delimiter=',')
#from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
#path = "data/ipl_matches_small.csv"
#print np.unique(ipl_matches_array[1:1452,3])
#print np.unique(ipl_matches_array[1:1452,4])
    get_unique_teams_set=int(len(np.union1d (np.unique(ipl_matches_array[1:1451,3]),np.unique(ipl_matches_array[1:1451,4]))))
    return get_unique_teams_set
# Enter Code Here
