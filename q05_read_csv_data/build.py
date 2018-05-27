import numpy as np

def read_ipl_data_csv(path, dtype='np.float64'):
    ipl_matches_array = np.genfromtxt(path, dtype, skip_header=1, delimiter=',')
    return ipl_matches_array
path = './data/ipl_matches_small.csv'
dtype = '|S50'

testArray = read_ipl_data_csv(path,dtype)
print(testArray)

