# Default imports
import numpy as np

# Enter code here
path = '/home/darshind/Workspace/code/python_intermediate_project/data/ipl_matches_small.csv'

def read_ipl_data_csv(path,dtype):
    read_ipl_data_csv = np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    return read_ipl_data_csv
print read_ipl_data_csv(path,dtype = '|S50')
