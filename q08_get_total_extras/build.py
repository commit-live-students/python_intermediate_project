# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    data = read_ipl_data_csv(path,dtype='|S50')
    extras = 0
    for d in data:
        extras += int(d[17])
    return extras
