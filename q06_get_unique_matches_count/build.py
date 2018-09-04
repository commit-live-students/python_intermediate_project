# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_unique_matches_count():
    array = np.genfromtxt(path,skip_header=1, delimiter=',', dtype='|S50')
    return len(np.unique(array[0:,0]))
    
import numpy as np
array = np.genfromtxt(path,skip_header=1, delimiter=',', dtype='|S50',autostrip=True)
print(len(np.unique(array[0:,0])))


