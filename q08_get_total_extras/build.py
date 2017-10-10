# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

def get_total_extras():
    ipl_matches_array = read_ipl_data_csv(path, np.int32)
    extras_column = ipl_matches_array[:,17]
    extras_sum = 0
    for i in extras_column:
        extras_sum += i
    return extras_sum
