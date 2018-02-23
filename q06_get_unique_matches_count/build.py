# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
# Enter Code Here
import numpy as np
import pandas as pd

def get_unique_matches_count():
    match_count = np.genfromtxt(path, skip_header = 1, delimiter =',')
    ipl_matches_array = np.unique(match_count[:,0]).size
    return ipl_matches_array

get_unique_matches_count()
