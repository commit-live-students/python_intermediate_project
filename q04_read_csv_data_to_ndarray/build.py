import numpy as np
path = "./data/ipl_matches_small.csv"
dttype = 'str'


def read_csv_data_to_ndarray(pathr, dttpye):
    read1 = np.loadtxt(pathr, delimiter = ',', skiprows= 1, dtype = dttype)


    #print type(read1)
    return read1
print read_csv_data_to_ndarray(path, dttype)
