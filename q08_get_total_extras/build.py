# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():
    data = read_ipl_data_csv(path,dtype=type(int))
    #extras=[x[17] for x in data[1:]]
    
    extras = data[:,17]
    ex =list(map(int ,extras)) 
    return np.sum(ex)
    

get_total_extras()




