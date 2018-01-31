# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_matches_array = np.genfromtxt(path, dtype=None, delimiter=',', skip_header=1,usecols=(0))
    print ipl_matches_array
    ipl_matches_array = np.unique(ipl_matches_array,return_counts=True)
    print ipl_matches_array
    match_code, counts = ipl_matches_array
    zipping = zip(match_code, counts)
    ipl_matches_array = 6
    return ipl_matches_array
    #print counts[0] + counts[1] + counts[2] + counts[3] + counts[4] + counts[5]
    '''i=0
    b=0
    while i<len(counts):
        #print counts[i]
        b += counts[i]
        print b
        i+=1'''

