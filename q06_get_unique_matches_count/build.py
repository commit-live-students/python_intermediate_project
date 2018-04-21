# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_matches_count():
    matchDataArray = read_ipl_data_csv(path,'|S50')
    #print(matchDataArray[:,0])
    #print(np.unique(matchDataArray[:,0]).size)
    return np.unique(matchDataArray[:,0]).size
get_unique_matches_count()

