# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    with open(path,'r') as f:
        reader=csv.reader(f, delimiter=',')
        header=next(reader)
        data=list(reader)
        arr=np.array(data)
        ar2=arr[0:,0:1]
        ar3=np.unique(ar2)
        ipl_matches_array=np.size(ar3)
        return ipl_matches_array
get_unique_matches_count()


