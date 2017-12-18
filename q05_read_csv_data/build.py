# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
#path = "./data/ipl_matches_small.csv"
#print read_ipl_data_csv('./data/ipl_matches_small.csv')
def read_ipl_data_csv(file_path, dtype='|S50'):
    ipl_matches_array = np.genfromtxt(file_path,delimiter=',',dtype='|S50',skip_header=1)
    return ipl_matches_array
