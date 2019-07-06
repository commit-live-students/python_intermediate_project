# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

def read_ipl_data_csv(file_path,dtype ):
    ipl_matches_array = np.genfromtxt(file_path, delimiter = ',', dtype = dtype,skip_header=1)
    return ipl_matches_array
    

ipl_matches_array=read_ipl_data_csv('./data/ipl_matches_small.csv', dtype = '|S50')
print(ipl_matches_array)


