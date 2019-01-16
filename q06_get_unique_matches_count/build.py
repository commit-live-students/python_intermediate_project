# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
#import numpy as np
from numpy import genfromtxt
import pandas as pd
path = 'data/ipl_matches_small.csv'

# Enter Code Here

matches = pd.read_csv('data/ipl_matches_small.csv')
#genfromtxt(path,delimiter=',',skip_header=1)
matches.head()
type(matches)
temp = matches['match_code'].nunique()
temp
def get_unique_matches_count():
   # data = genfromtxt(path,delimiter=',',skip_header=1)
   # ipl_matches_array = np.unique(data,return_counts = True)
    ipl_matches_array = matches['match_code'].nunique()
    return ipl_matches_array
get_unique_matches_count()



