# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    sum=0
    ipl_matches_array=read_ipl_data_csv(path,'|S50')
    ext=ipl_matches_array[:,17].astype(np.float16)
    for i in ext:
        sum=sum+i
# Enter Code Here
    return sum
