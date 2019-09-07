# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    num_of_chars = 100
    ipl_matches_array  = np.genfromtxt(path,dtype=(np.str_, num_of_chars), delimiter=",", skip_header=1)
    match_id_array = np.unique(ipl_matches_array[:,0])
    match_count = len(match_id_array)
    return match_count
