#%load q04_read_csv_data_to_ndarray/build.py

import numpy as np

path='./data/ipl_matches_small.csv'
dtype= '|S20'
def read_csv_data_to_ndarray(path,dtype):
    
    arr=np.genfromtxt(path,delimiter=',',dtype=dtype,skip_header=1)
#print(type(arr))
#print(arr.dtype)

    
    return arr

read_csv_data_to_ndarray(path,dtype)




