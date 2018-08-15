# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    count=0
    data=np.genfromtxt(path,delimiter=',')
    extras=data[1:,17]
    runs=np.sum(extras,dtype=int)
    return runs
    

get_total_extras()


