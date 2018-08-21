# %load q08_get_total_extras/build.py
# Default Imports
import pandas as pd
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_data = pd.read_csv(path)
    ipl_df = pd.DataFrame(ipl_data)
    return ipl_df['extras'].sum()

get_total_extras()

