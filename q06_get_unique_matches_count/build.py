# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = np.genfromtxt(path,dtype='|S100', skip_header=1, delimiter=",")
    return (np.unique(ipl_matches_array[:,0])).size
