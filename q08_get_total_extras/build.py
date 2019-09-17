# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
from numpy import genfromtxt

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    read_data = read_ipl_data_csv(path,dtype = 'int16')

    extras = read_data[:,17]
    sum_of_extras = extras.sum()
    print (sum_of_extras)
    return sum_of_extras
