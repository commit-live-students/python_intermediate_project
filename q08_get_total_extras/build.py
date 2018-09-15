# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import csv

path = 'data/ipl_matches_small.csv'
def get_total_extras():
    
    
    a = np.genfromtxt(path,dtype=None,delimiter=',',skip_header=1) #readfile
    
   
    extras = []  #Creating list to store extra runs.
    
    
    for i,v in enumerate(a): #looping through list
        extras.append(a[i][17])  #extras column index(17th is the order)
    return sum(extras)
get_total_extras()

        
    

    
    











