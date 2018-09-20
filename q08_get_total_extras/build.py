# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_extra = read_ipl_data_csv(path, dtype = '|S50')
    sum_extra = np.array(ipl_extra[:,17],dtype = int).sum()
    return sum_extra
get_total_extras()
    

