# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
Count = 0
def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path,"|S50")
    column =  ipl_matches_array[:,0]
    Count = len(np.unique(column))
    return Count
