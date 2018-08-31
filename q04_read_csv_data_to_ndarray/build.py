# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
def read_csv_data_to_ndarray(path,dtype):
    
    my_data = np.genfromtxt(path, dtype, skip_header=1, delimiter =',')
    my_data = np.array(my_data)
    return my_data 
read_csv_data_to_ndarray('data/ipl_matches_small.csv','float')


