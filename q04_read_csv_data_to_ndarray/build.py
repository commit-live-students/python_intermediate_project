import numpy as np
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(p,dt=np.float64):
    f = np.genfromtxt(fname=p,dtype=dt,delimiter=',',skip_header=1)
    return f

ipl = read_csv_data_to_ndarray(path)
