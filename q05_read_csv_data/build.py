import numpy as np

path = './data/ipl_matches_small.csv'
def read_ipl_data_csv(path,dtype='|S50'):
    ipl_matches_array = np.genfromtxt(path, dtype=dtype, delimiter=',',skip_header=1)
    return ipl_matches_array

#read_ipl_data_csv(path)

