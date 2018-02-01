# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndwarray(path, dtype):
    array = np.loadtext(path, dtype)
    return array
