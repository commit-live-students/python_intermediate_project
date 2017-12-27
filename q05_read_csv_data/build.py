import numpy as np
path = "./data/ipl_matches_small.csv"

def read_ipl_data_csv(filepath,dtype='|S50'):
    f = np.genfromtxt(filepath,dtype,delimiter=',',skip_header=1)
    return f

ipl_matches_array = read_ipl_data_csv(path)
