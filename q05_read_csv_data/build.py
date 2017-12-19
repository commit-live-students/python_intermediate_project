# Default imports
import numpy as np
def read_ipl_data_csv(path, dtype='|S50'):
    numpy_array = np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    return numpy_array
