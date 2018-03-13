# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    read_data = read_ipl_data_csv(path, dtype = '|S50')
    match_extras = read_data[:,17]
    extras = 0
    for i in match_extras:
        extras += int(i)
        
    return extras

get_total_extras()
    


