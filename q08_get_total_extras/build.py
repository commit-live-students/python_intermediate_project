# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    varfile=np.genfromtxt(path,delimiter=',',skip_header=1,dtype='int16')
    return np.sum(varfile[:,17])
get_total_extras()


