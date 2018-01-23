# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    data=read_ipl_data_csv(path,'|S50')
    uu = np.unique(data[:,0])
    ipl_matches_array = np.unique(data[:,0]).size
    return ipl_matches_array
