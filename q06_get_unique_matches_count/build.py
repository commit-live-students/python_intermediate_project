# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
# Enter Code Here
def get_unique_matches_count():

    data = read_ipl_data_csv(path,'|S50')
    match_codes = data[:,0:1]
    unique_count = len(np.unique(match_codes))
    return unique_count

get_unique_matches_count()
