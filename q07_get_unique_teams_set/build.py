# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np



def get_unique_teams_set() :
    ipl_matches_array = read_ipl_data_csv(path,dtype = "|S50")
    unique_teams = np.union1d(np.unique(ipl_matches_array[:,3]),np.unique(ipl_matches_array[:,4]))
    seta = set(unique_teams)
    return seta

get_unique_teams_set()
# Enter Code Here
