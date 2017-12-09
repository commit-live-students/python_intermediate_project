# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np

# Enter Code Here
def get_unique_teams_set():
    arr = read_ipl_data_csv(path,dtype='|S100')
    return set(np.unique(arr[:,3:5]))
