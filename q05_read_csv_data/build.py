# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

def read_ipl_data_csv():
    path = './data/ipl_matches_small.csv'
    ipl_matches_array = np.genfromtxt(path, delimiter=',',dtype='|S50')
    return ipl_matches_array

read_ipl_data_csv()
    
# Enter code here


