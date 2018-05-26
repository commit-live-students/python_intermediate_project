import numpy as np

def read_csv_data_to_ndarray(path, dtype='np.float64'):
    iplstats = np.genfromtxt(path, dtype, skip_header=1, delimiter=',')
    return iplstats
path = './data/ipl_matches_small.csv'
dtype = '|S100'

testArray = read_csv_data_to_ndarray(path,dtype)
print(testArray)

