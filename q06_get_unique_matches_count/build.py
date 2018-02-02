# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_matches_count():
    narray = np.genfromtxt(path, dtype=np.float, skip_header=1, delimiter=',')
    matches = narray[:,0] # get list of all match codes only
    #print type(matches)

    unique_matches = np.unique(matches, return_counts=False)
    ipl_matches_array = len(unique_matches)
    print ipl_matches_array
    #print type(ipl_matches_array)
    return ipl_matches_array

#get_unique_matches_count()
