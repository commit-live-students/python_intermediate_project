# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    df = read_ipl_data_csv(path,'str')
    extras_arr = df[:,17]
    sum=0
    for i in extras_arr:
        sum += int(i)
    return(sum)

get_total_extras()

