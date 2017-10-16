# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

#path = 'data/ipl_matches_small.csv'
import numpy as np
from numpy import genfromtxt
def get_total_extras() :
    ipl_matches_array = genfromtxt("./data/ipl_matches_small.csv", delimiter=',', skip_header = 1)
    #print ipl_matches_array
    extras = ipl_matches_array[:,17]
    Sum = ipl_matches_array[:,17].sum().astype(int)
    return Sum

# Enter Code Here
