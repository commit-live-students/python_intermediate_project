# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np

def get_unique_matches_count():
    matches = read_ipl_data_csv(path,'|S50')[:,0]
    return len(np.unique(matches))
