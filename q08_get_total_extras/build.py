# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    new = read_ipl_data_csv(path, dtype='|S50')
    no_of_extras = new[:,-6]
    sum_extras = np.sum(no_of_extras.astype(np.int8))
    return sum_extras
    
get_total_extras()
