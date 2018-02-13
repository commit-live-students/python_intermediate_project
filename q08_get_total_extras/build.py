# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    data = read_ipl_data_csv(path, '|S50')
    count = data[:,-6]
    conv_int = count.astype(int)
    extras = sum(conv_int)
    return extras

print get_total_extras()
