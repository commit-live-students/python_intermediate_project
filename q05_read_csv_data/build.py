# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

path = './data/ipl_matches_small.csv'



def read_ipl_data_csv(path):
    return np.genfromtxt(path,skip_header=1,delimiter=',')

print read_ipl_data_csv(path)
