# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
# Enter code here
def read_ipl_data_csv(path,dtype=np.float64):

    data =  np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)

    return data

ipl_matches_array = read_ipl_data_csv(path,'|S50')
print ipl_matches_array.shape
print ipl_matches_array.dtype
