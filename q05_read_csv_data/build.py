# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

def read_ipl_data_csv(path,dtype):
    csvFileOut = np.genfromtxt(path,skip_header = 1,dtype = dtype , delimiter = ',')
    print(csvFileOut.shape)
    return csvFileOut
read_ipl_data_csv('data/ipl_matches_small.csv', dtype='|S50')
# Enter code here

