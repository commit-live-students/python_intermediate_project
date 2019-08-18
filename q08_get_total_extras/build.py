# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():
    result = read_ipl_data_csv(path,dtype = '|S50')
    extras = result[0:,17].astype(int)
    total_extras = extras.sum(axis=0, dtype = np.int32)
    return total_extras
