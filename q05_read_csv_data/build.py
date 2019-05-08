# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

path = './data/ipl_matches_small.csv'

# Enter code here
def read_ipl_data_csv(path, dtype=np.float):
    data = np.genfromtxt(path, dtype, delimiter=',', skip_header=1)
    return data

ipl_matches_array = read_ipl_data_csv(path, dtype='|S50')



