# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import pandas as pd

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    
    df=pd.read_csv(path)
    extra_sum=df['extras'].sum()
    
    return extra_sum

get_total_extras()
# Enter Code Here


