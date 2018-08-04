# %load q05_read_csv_data/build.py
# Default imports
path = './data/ipl_matches_small.csv'
import numpy as np

# Enter code here
def read_ipl_data_csv():
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', skip_header=1, delimiter=',')
    return ipl_matches_array


