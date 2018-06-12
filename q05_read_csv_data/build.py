# Default imports
import numpy as np

def read_ipl_data_csv(path, dtype=np.float64):
    return  np.genfromtxt(fname=path,dtype=dtype, delimiter=",",skip_header=True)
