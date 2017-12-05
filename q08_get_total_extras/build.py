# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    actual_data = read_ipl_data_csv(path, dtype='|S50')
    all_extras = actual_data[:,17:18]
    total_extras = all_extras.astype(np.int16).sum()
    return total_extras


print get_total_extras()
