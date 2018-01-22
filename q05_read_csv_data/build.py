# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
# Enter code here
def read_ipl_data_csv(path, dtype=('|S50')):
    ipl_matches_array1 = np.genfromtxt(path,dtype=('|S50'),delimiter=',')
    ipl_matches_array = np.delete(ipl_matches_array1,0,0)
    return ipl_matches_array
