# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtype = float
# Enter code here
def read_csv_data_to_ndarray(path,dtype):
    main_arr = np.genfromtxt(path,dtype=dtype,skip_header=1,delimiter=',')
    #print(main_arr)
    return main_arr
#read_csv_data_to_ndarray(path,dtype)



