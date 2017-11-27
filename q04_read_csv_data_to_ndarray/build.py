# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype = np.float64):
    ipl_file = np.genfromtxt(path,dtype = dtype,skip_header=1,delimiter=',')
    ipl_file_array_n = np.array(ipl_file)
    return ipl_file_array_n
