# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import csv

path = 'data/ipl_matches_small.csv'

def get_total_extras():
     with open(path,'r') as f:
        reader=csv.reader(f, delimiter=',')
        header=next(reader)
        data=list(reader)
        arr=np.array(data)
        extras=np.hstack(arr[0:,17:18])
        arr=np.array(extras, dtype=np.int32)
        data=list(arr)
        return np.sum(data)
get_total_extras()


