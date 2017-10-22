# Default Imports
import numpy as np
path = "/home/darshind/Workspace/code/python_intermediate_project/data/ipl_matches_small.csv"

# Enter code here

def read_csv_data_to_ndarray(path,delimiter):
    data = np.genfromtxt(path,delimiter=',',skip_header= 1,dtype='|S100')
    return data
print read_csv_data_to_ndarray(path,delimiter=',')
