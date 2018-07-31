# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
dtype = '|S50'
# Enter Code Here
import numpy as np
def get_unique_matches_count():
    ipl = np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
    ipl_matches_array= ipl[:,0]
    uni = len(np.unique(ipl_matches_array))
    return uni
get_unique_matches_count()

