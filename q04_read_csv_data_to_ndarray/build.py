# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, dtype=np.float64):
    file_data = np.genfromtxt(path,skip_header=1,dtype=dtype,delimiter=',')
    return file_data

print read_csv_data_to_ndarray('data/ipl_matches_small.csv',None)
#print read_csv_data_to_ndarray('/home/Mohammed-Sunasra/Workspace/code/python_intermediate_project/data/ipl_matches_small.csv')
