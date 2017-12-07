import numpy as np

path = "./data/ipl_matches_small.csv"
dttype = 'str'

def read_csv_data_to_ndarray(path_par, dttype):
    data = np.loadtxt(path_par, delimiter=",", skiprows=1,dtype=dttype)
    return data

print read_csv_data_to_ndarray(path, dttype)
