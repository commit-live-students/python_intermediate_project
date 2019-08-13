# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    
    #reading file using np.genfromtxt
    a = np.genfromtxt(path,dtype=None,delimiter=',',skip_header=1)
    
    #Creating an empty list to store extra runs.
    extras = []
    
    #Looping thru each deliveries' extra and storing the value in list
    for i,v in enumerate(a):
        extras.append(a[i][17])  #17th index is the extra column
    return sum(extras)
get_total_extras()


