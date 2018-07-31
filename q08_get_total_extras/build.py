# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    data = read_ipl_data_csv(path, dtype = int)
    #print(data)
    extra = 0
    for row in data:
        extra+=row[17]
    #print(extra==88)
    return int(extra)
    
    
#get_total_extras()


