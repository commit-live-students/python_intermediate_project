# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"
# Enter code here
def read_ipl_data_csv(path,dtype=np.float64):
	ipl_matches_array =  np.genfromtxt(path,delimiter=',',skip_header=1,dtype= '|S50')
	return ipl_matches_array
