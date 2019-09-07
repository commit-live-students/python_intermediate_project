# Default imports
import numpy as np

def read_ipl_data_csv(f_path, **inp_dtype):
    if "dtype" in inp_dtype:
        ipl_match = np.genfromtxt(f_path,dtype=inp_dtype["dtype"], delimiter=",", skip_header=1)
    else:
        print "dtype key not found in argument, USAGE [read_csv_data_to_ndarray(f_path,dtype=<>)]"
        raise KeyError
    return ipl_match
