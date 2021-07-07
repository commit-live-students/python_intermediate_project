
import numpy as np 
def read_csv_data_to_ndarray(path,dtype):
    #path='../Data/ipl_matches_small.csv'
    #dtype=np.float64
    ipl=np.genfromtxt(path, dtype, skip_header=1, delimiter=',')
    return ipl
read_csv_data_to_ndarray('data/ipl_matches_small.csv',np.float64)


