# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path, dtype='|S50'):
    csv = np.genfromtxt(path,delimiter=",",skip_header=1,dtype=dtype)
    return csv
