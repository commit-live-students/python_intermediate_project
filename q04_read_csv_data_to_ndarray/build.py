import numpy as np
path = './data/ipl_matches_small.csv'

def read_csv_data_to_ndarray(path,inputDtype):
    ipl_data = np.genfromtxt(path,dtype=inputDtype,skip_header=True, delimiter=',')
    return ipl_data
data = read_csv_data_to_ndarray(path,'|S20')
print(data.shape)
print(data.dtype)


