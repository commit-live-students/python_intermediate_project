# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"
def read_csv_data_to_ndarray(path,dtype):
    numpy_array=np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)
    return numpy_array
