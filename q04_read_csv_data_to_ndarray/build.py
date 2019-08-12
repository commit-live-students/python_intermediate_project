# Default Imports
import numpy as np
#path = "./data/ipl_matches_small.csv"
def read_csv_data_to_ndarray(file_path, dat_typ):
    matches = np.genfromtxt(file_path,delimiter=',',dtype=dat_typ,skip_header=1)
    return matches
