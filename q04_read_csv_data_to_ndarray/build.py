import numpy as np
path = "./data/ipl_matches_small.csv"

#def read_csv_data_to_ndarray(path,datype=np.float64):
def read_csv_data_to_ndarray(path,data_type=np.float64):
    my_data=np.genfromtxt(path,delimiter=",", skip_header=1,dtype=data_type)
    return my_data
