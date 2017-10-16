# Default imports
import numpy as np
from numpy import genfromtxt
# path = "./data/ipl_matches_small.csv"

# Enter code herefrom numpy import genfromtxt
def read_ipl_data_csv(path, dtype = '|S20') :
    ipl_matches_array = genfromtxt(path, dtype, delimiter=',', skip_header = 1)
    return ipl_matches_array

# Enter code here
