# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

path = './data/ipl_matches_small.csv'

def read_ipl_data_csv(path,dtype = '|S50'):
    arr = np.genfromtxt(fname = path, delimiter=',',dtype = dtype, skip_header=1)
    return (arr)
    # Enter code here
read_ipl_data_csv(path)


