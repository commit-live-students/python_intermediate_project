# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
from inspect import getfullargspec
path = 'data/ipl_matches_small.csv'

def read_csv_data_to_ndarray(path,input_dtype = np.float64):
   data = np.genfromtxt(path,dtype = input_dtype,delimiter = ',',skip_header = 1)
   #args = getfullargspec(read_csv_data_to_ndarray)
   #print(len(args[0]))
   #print(data.shape)
   #print(data.dtype)
   return data

# Enter code here
#read_csv_data_to_ndarray(path,'|S100')


