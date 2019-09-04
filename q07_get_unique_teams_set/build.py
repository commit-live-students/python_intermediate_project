# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    data=read_ipl_data_csv(path,'|S50')
    n1 = np.unique(data[:,3])
    n2 = np.unique(data[:,4])
    return set(np.union1d(n1,n2))
