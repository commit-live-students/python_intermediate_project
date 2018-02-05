# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
from numpy import genfromtxt
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():

    #my_data = read_ipl_data_csv
    my_data = genfromtxt(path,delimiter=',',dtype = '|S50', skip_header = 1)
    match_id = my_data[:,0]
    ipl_matches_array = np.unique(match_id)

    return len(ipl_matches_array)
