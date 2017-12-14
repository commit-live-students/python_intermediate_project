# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
def get_unique_matches_count():
    ipl_data = read_ipl_data_csv(path=path,dtype='|S50')
    ipl_matches_array = len(np.unique(ipl_data[:,0]))
    return ipl_matches_array

#print get_unique_matches_count()
