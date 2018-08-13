# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    new = read_ipl_data_csv(path,dtype='int32')
    extras = new[:,17]
    #print ((extras[:]))
    sum_extras = extras.sum()
    print (sum_extras)
    return sum_extras
