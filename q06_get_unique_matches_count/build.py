# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here

import numpy as np 
import csv

def get_unique_matches_count():
    
    ipl_matches_array = []
    with open (path) as csvfile:
        reader = csv.reader(csvfile)
        for x in reader:
            ipl_matches_array.append(x)
        header = tuple(ipl_matches_array[0])
        matches = np.unique([x[0]for x in ipl_matches_array[1:]])
        
        count = len(matches)
        
    return count
        
       

            
            
get_unique_matches_count()


