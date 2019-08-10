# Default imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_ipl_data_csv(path=path,dtype='|S50'):
    my_data = np.genfromtxt(path, delimiter=',',skip_header=1,dtype=dtype)
    return my_data


# Enter code here
