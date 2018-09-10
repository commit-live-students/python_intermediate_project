# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path, dtype= '|S50'):
        ipl_matches_array= np.loadtxt('./data/ipl_matches_small.csv', delimiter=',', dtype= '|S50', skiprows=1)
    

        return ipl_matches_array    
read_ipl_data_csv


