# %load q04_read_csv_data_to_ndarray/build.py
import numpy as np
path = './data/ipl_matches_small.csv'
dtype = float
def read_csv_data_to_ndarray():
    my_data = np.genfromtxt(path,dtype=dtype,skip_header =1,delimiter=',')
    return my_data

read_csv_data_to_ndarray()

# Enter code here

T



