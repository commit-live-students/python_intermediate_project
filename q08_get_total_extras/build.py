# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

import numpy as np
# Enter Code Here

def get_total_extras():
    array=read_ipl_data_csv(path,np.int64)
    return array[:,17:18].sum()


