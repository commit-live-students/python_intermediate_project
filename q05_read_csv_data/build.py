# Default imports
import numpy as np

# Enter code here
path = "./data/ipl_matches_small.csv"
def read_ipl_data_csv(path,dtype='|S50'):
    return np.genfromtxt(path, delimiter=",",dtype=dtype)[1:,]
ipl_matches_array = read_ipl_data_csv(path)
