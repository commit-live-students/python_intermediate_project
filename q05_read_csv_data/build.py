
import numpy as np


def read_ipl_data_csv(path, dtype):
    # transform data into numpy array
    data = np.genfromtxt(path,dtype, delimiter=',', skip_header=1)
    return data
read_ipl_data_csv('data/ipl_matches_small.csv', '|S50')


