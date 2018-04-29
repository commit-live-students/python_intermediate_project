# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    file_data = read_ipl_data_csv(path, dtype='|S50')
    col1_array = file_data[:,0]
    col1_unique = np.unique(col1_array)
    col_uniq_count = len(col1_unique)
    return col_uniq_count
    

