# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_df = read_ipl_data_csv(path,dtype = 'S50')
    ipl_new = ipl_df[:,17].astype(int)
    ipl_sum = np.sum(ipl_new)
    return ipl_sum
    


