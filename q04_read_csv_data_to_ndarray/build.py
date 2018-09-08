import numpy as np
def read_csv_data_to_ndarray(path,types) :
    nump=np.genfromtxt(path,delimiter=',',dtype=types)
    return nump[1:]

