# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = './data/ipl_matches_small.csv'
# Enter code here
def read_ipl_data_csv():
    ipl_matches_array = np.genfromtxt(path, delimiter=',',dtype=None)
    return ipl_matches_array
read_ipl_data_csv()


