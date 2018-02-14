import numpy as np
from io import BytesIO

path = "./data/ipl_matches_small.csv"

def read_ipl_data_csv():
    ipl_matches_array=np.genfromtxt(BytesIO(path),skip_header=1,delimiter=",",dtype="|S50")
    return ipl_matches_array
