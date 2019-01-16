# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import pandas as pd

path = 'data/ipl_matches_small.csv'

# Enter Code Here
matches = pd.read_csv(path)
matches['extras'].sum()
def get_total_extras ():
    extras = matches['extras'].sum()
    return extras
get_total_extras()

