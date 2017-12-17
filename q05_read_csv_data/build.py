# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_ipl_data_csv(path, dtype = '|S50'):
    csv_data = np.genfromtxt(path, delimiter = ',',dtype = dtype,skip_header= True)
    return csv_data

ipl_matches_array = read_ipl_data_csv(path, dtype='|S50')
#print type(ipl_matches_array)
#print ipl_matches_array.dtype
#print ipl_matches_array.shape
