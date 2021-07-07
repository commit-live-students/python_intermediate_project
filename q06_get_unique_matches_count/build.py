# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here

def get_unique_matches_count():
    ipl_matches = np.genfromtxt(path,delimiter=",",dtype='|S50',skip_header=1)
    ipl_matches1 = ipl_matches[:,0]
    ipl_matches2 = np.unique(ipl_matches1)
    return ipl_matches2.size
