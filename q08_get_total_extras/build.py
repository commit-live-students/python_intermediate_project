# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_matches= np.array(read_ipl_data_csv(path,'|S50'))
    extras= np.array(ipl_matches[0:,17],dtype=np.int8)
    return int(extras.sum())
