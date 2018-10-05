# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
import pandas as pd

def get_unique_matches_count():
    data2=pd.read_csv(path,delimiter=',',dtype='|S50')
    ipl_matches_array=data2.iloc[:,0:1].nunique()
    return(ipl_matches_array[0])
get_unique_matches_count()


