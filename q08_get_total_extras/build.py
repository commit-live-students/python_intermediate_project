# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import pandas as pd
path = 'data/ipl_matches_small.csv'
data = pd.read_csv(path)
# Enter Code Here
def get_total_extras():
    a = data['extras'].sum()
    return a
b= get_total_extras()
b


