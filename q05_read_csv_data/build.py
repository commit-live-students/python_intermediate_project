# Default imports
import numpy as np

path = "./data/ipl_matches_small.csv"

def read_ipl_data_csv(path, dtype = '|S50'):
    ipl_array = np.genfromtxt(path,delimiter=',',  dtype = dtype, skip_header= 1 )
    return ipl_array

ipl_matches_array = read_ipl_data_csv(path)
