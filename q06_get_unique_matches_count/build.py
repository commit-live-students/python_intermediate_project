# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
import pandas as pd
import csv
# Enter Code Here
def get_unique_matches_count(path=path):
    l=[]
    ipl_matches_array=0
    with open(path) as csvfile:
        data=csv.reader(csvfile,delimiter=',')
        for rows in data:
            l.append(rows)
        
    l=np.array(l)
   
    ipl_matches_array=len(np.unique(l[1:,0]))
    return (ipl_matches_array)
        
    
#get_unique_matches_count()
    



    


