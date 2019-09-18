# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
import pandas as pd
# Enter Code Here
#a = np.genfromtxt(path , delimiter=',',skip_header=1, dtype='|S50')
def get_unique_matches_count():
    my_data = np.genfromtxt(path, delimiter=',', dtype='|S50', skip_header=1)
    unique_matches = np.unique(my_data[:,0])
    ipl_matches_array = unique_matches.size
    return ipl_matches_array
get_unique_matches_count()


#print len(a)

#filename.close    
