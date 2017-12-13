# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path=path,dtype=np.float64):
    csvData = np.genfromtxt(path, delimiter=',', dtype=dtype, skip_header=1)
    return csvData

#print read_csv_data_to_ndarray(dtype=np.int)
print read_csv_data_to_ndarray()
print type(read_csv_data_to_ndarray())
