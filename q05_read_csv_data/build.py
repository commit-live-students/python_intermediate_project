# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
def read_ipl_data_csv(path,dtype=np.float64):
    path1 = np.genfromtxt(path,dtype=dtype,skip_header = 1,delimiter=',')
    print(path1.shape)
    return path1
read_ipl_data_csv(path,dtype='|S50')


