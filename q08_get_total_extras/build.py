# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    i_total_extras = 0
    ipl_match_array = read_ipl_data_csv(path,dtype='|S200')
    i_total_extras = np.sum(ipl_match_array[:,17].astype(int))
    return i_total_extras
