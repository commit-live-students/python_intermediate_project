# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
def get_total_extras(path=path,dtype=None):
    x= np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1,usecols=17)
    
    return sum(x)    
    
    
# Enter Code Here
get_total_extras()



