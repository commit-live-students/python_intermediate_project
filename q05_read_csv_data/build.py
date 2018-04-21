import numpy as np
def read_ipl_data_csv(path,dtype=None):
    ipl_matches=np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)
    return (ipl_matches)


