# Default Imports
import numpy as np
path = "../data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,input_dtype=np.float64):
    ipl_array = np.genfromtxt(path, delimiter=",",dtype=input_dtype,skip_header=1)
    return ipl_array
#op_arr = read_csv_data_to_ndarray(path,'|S100')
#print op_arr.shape
#print op_arr.dtype
