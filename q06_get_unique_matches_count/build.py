# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
data = read_ipl_data_csv(path,dtype='|S50')

def get_unique_matches_count():
    ipl_matches_array = np.unique(data[:,0]).shape[0]
    return ipl_matches_array
