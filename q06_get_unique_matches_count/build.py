# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
#from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():

    ipl_matches_array = np.genfromtxt(path,dtype='|S50',delimiter=',',skip_header=1)
    count=int(len(np.unique(ipl_matches_array[0:,0])))
    return count
