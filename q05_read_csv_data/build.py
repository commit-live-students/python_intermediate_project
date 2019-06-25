# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

path = './data/ipl_matches_small.csv'

def read_ipl_data_csv(path,dtype=type(float)):
    ipl_array = np.genfromtxt(path,dtype=dtype,skip_header=1, delimiter=',')
    return ipl_array
# Enter code here

print(read_ipl_data_csv(path,'|S50'))



