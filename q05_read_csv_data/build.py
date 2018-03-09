# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
def read_ipl_data_csv(path,dtype):
    data = np.genfromtxt("path", dtype="|S50", skip_header=1, delimiter=",")
    return data
# Enter code here
#print read_ipl_data_csv(path,float)
