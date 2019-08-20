# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here

def get_unique_matches_count():
    matchdata = read_ipl_data_csv(path,dtype='|S50')
    ipl_matches_array = len(np.unique(matchdata[:,[0]]))
    return ipl_matches_array
