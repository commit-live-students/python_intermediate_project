# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    #read_ipl_data_csv()
    data = read_ipl_data_csv(path,dtype='|S100')
    #ipl_matches_array=np.unique()
    unique_count=np.unique(data[:,0])
    return len(unique_count)
get_unique_matches_count()


