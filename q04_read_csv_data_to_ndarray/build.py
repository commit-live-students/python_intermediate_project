# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path, dtyp):
    ipl_array=np.genfromtxt(path, dtype=dtyp, skip_header=1, delimiter=',')
    return(ipl_array)
    
read_csv_data_to_ndarray(path, np.float)


