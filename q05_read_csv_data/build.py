# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path, dtype=np.float64):
    return  np.genfromtxt(fname=path,dtype=dtype, delimiter=",",skip_header=True)
