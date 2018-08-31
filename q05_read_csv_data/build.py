# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = 'data/ipl_matches_small.csv'
def read_ipl_data_csv(path,dtype):
    
    ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype, delimiter=',')
    ipl_matches_array = np.array(ipl_matches_array)
    return(ipl_matches_array)
    


read_ipl_data_csv('data/ipl_matches_small.csv','|S50')



