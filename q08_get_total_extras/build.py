# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
def get_total_extras():
    file_data = read_ipl_data_csv(path, dtype='|S50')
    extras_col =list(file_data[:,17])
    extras_list= [int(x) for x in extras_col]
    extras=0
    for i in range(0,len(extras_list),1):
        if extras_list[i]!=0:
            extras+=extras_list[i]
    return extras

    
# Enter Code Here

