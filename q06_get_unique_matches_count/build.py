# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
from numpy import genfromtxt
# path = "./data/ipl_matches_small.csv"

# Enter code herefrom numpy import genfromtxt
def get_unique_matches_count() :
    ipl_matches_array = genfromtxt("./data/ipl_matches_small.csv", dtype = '|S20', delimiter=',', skip_header = 0)
    # print ipl_matches_array[:,0]
    counts = np.unique(ipl_matches_array[:,0])
    return (len(counts) - 1)
