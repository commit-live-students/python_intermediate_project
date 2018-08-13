# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
#from read_ipl_data_csv import ipl_matches_array
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_matches_count():
    data_index = read_ipl_data_csv(path,dtype=np.int64)
    new_data = data_index[:,0]
    ipl_matches = np.unique(new_data)
    ipl_matches_array = ipl_matches.size
    return ipl_matches_array
print get_unique_matches_count()
