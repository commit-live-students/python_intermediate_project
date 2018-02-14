# Default Imports
import numpy as np
from io import BytesIO
path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray():
    arr=np.genfromtxt(BytesIO(path),skip_header=1,delimiter=",",dtype=np.float64)
    return a
