# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
# Enter code here
load = np.genfromtxt(str(path),delimiter=',')
load


