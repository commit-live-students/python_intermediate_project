# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# load data from csv filw with ',' as delimiters
def read_csv_data_to_ndarray(path,dtype = '|S30'):
    data = np.loadtxt(fname=path,delimiter=',',dtype=dtype,skiprows =1)
    return data

#call function and print data
print(read_csv_data_to_ndarray(path))   


