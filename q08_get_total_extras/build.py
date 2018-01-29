# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    iplmatch= read_ipl_data_csv(path,dtype='int64')
    extra=iplmatch[:,17]
    extra_sum = extra.sum()
    #print(extra_sum)
    return extra_sum
