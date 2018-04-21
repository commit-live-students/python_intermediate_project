import numpy as np
def read_csv_data_to_ndarray(path,dtype=np.float64):
    weather = np.genfromtxt(path, dtype=dtype, skip_header=1, delimiter=',')

    return(weather)

