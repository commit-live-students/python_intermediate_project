# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    path = 'data/ipl_matches_small.csv'
    a = read_ipl_data_csv (path,dtype='int32')
    extras = a[...,17]
    total_extras = extras.sum()
    return total_extras
