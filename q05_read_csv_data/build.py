
import numpy as np
def read_ipl_data_csv(path,dtype):
    ipl_matches_array = np.genfromtxt(path, dtype, skip_header=1, delimiter=',')
    return ipl_matches_array
read_ipl_data_csv('data/ipl_matches_small.csv','|S50')


