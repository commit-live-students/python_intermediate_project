# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_matches_array = np.genfromtxt(path, dtype=None, delimiter=',', skip_header=1,usecols=(0)) #read csv file
    ipl_matches_array = np.unique(ipl_matches_array,return_counts=True) #find unique values
    match_code, counts = ipl_matches_array #saperate unique values and their counts
    #zipping  = zip(match_code, counts) #zip those together. It is an unnecessary step.
    zipping = np.array(counts)
    return zipping.size


