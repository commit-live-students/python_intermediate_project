# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np
# Enter Code Here
def get_unique_teams_set():
    ipl_matches_array = np.genfromtxt(path,dtype='|S50',skip_header=1, delimiter=",")
    m1 = np.unique(ipl_matches_array[:,3])
    m2 = np.unique(ipl_matches_array[:,4])
    matches = np.union1d(m1,m2)
    return set(matches)

get_unique_teams_set()
