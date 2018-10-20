# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

import numpy as np 
# Enter Code Here
def get_total_extras():
    extras_array=np.genfromtxt(path, delimiter=',',dtype=int)[1:,[17]]
    return np.sum(extras_array)
get_total_extras()

