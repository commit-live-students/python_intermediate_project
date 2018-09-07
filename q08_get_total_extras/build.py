# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():
    ipl_data = read_ipl_data_csv(path, dtype='S50')
    print(ipl_data.shape)
    extras_data = ipl_data[:,-6].astype(int)
    print(extras_data)
    extras1 = np.sum(extras_data)
    
    return extras1




