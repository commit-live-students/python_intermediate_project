# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(link,data_type):
    f1 = np.genfromtxt(link, delimiter=',', dtype=data_type,skip_header=1)
    return f1

read_csv_data_to_ndarray(path,'|S20')
