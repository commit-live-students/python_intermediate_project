# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
import pandas as pd
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
tq=0

def get_unique_matches_count():
    arr1 = pd.read_csv(path)
    arr1=arr1['date'].unique()
    ipl_matches_array= len(arr1)
    return ipl_matches_array
get_unique_matches_count()




