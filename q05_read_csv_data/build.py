# Default imports
import numpy as np

path = "./data/ipl_matches_small.csv"

# Enter code here
def read_ipl_data_csv(path,dtype='|S50'):
    ipl_matches_array=np.genfromtxt(path,dtype,skip_header=1,delimiter=",")
    return ipl_matches_array
