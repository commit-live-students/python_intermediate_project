# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path , dtype ='|S50'):
    ipl_matches_array = np.genfromtxt(path, dtype = dtype, skip_header = 1, delimiter = ',')
    return ipl_matches_array
#read_ipl_data_csv('path')
    
    
read_ipl_data_csv('path')


