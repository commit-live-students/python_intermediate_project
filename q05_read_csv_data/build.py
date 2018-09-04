import numpy as np
path = './data/ipl_matches_small.csv'

def read_ipl_data_csv(path, dtype = 'float'):
    ipl_mathces_array = np.genfromtxt(path, dtype = '|S50', skip_header=1, delimiter=',')
    return ipl_mathces_array


