# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv

# Enter Code Here
def get_unique_matches_count():
    path = "data/ipl_matches_small.csv"
    ipl_matches_array = np.genfromtxt(path, dtype='|S50', delimiter=',', skip_header=True)
    return len(np.unique(ipl_matches_array[:,0]))
