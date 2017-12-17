# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"
datatype = float
#print datatype

# Enter code here
def read_csv_data_to_ndarray(path, datatype = np.float64):
    csv_data = np.genfromtxt(path, delimiter = ',', dtype = datatype ,skip_header= True)
    #print datatype
    #print type(datatype)
    #csv_data = np.dtype(csv_data, 'np.float64')
    return csv_data

#read =  read_csv_data_to_ndarray(path, datatype)

#print type(read)
#print read.dtype
