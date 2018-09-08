# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

import numpy as np
import csv
# Enter Code Here
def get_unique_matches_count():
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = list(reader)
        arr=np.array(data)
        ar2=arr[0:,0:1]
        ar3=np.unique(ar2)
        ipl_matches_array=np.size(ar3)
        return ipl_matches_array
get_unique_matches_count()
get_unique_matches_count()
path = 'data/ipl_matches_small.csv'
import csv
with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = list(reader)
        arr=np.array(data)
        ar2=arr[0:,0:1]
        ar3=np.unique(ar2)
        type(ar3)

        
       
type(ar3)
np.size(ar3)


