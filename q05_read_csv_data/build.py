import numpy as np
from q04_read_csv_data_to_ndarray.build import read_csv_data_to_ndarray

path = "./data/ipl_matches_small.csv"

def read_ipl_data_csv(path, dtype = "|S50"):

    ipl_matches_array = read_csv_data_to_ndarray(path, dtype)
    return ipl_matches_array
