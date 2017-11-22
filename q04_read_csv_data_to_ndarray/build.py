# Default Imports
import numpy as np
import os
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path, dtype=np.float64):
    """
    function that returns a numpy array when given a path to csv file
    """
    # my_path = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(my_path, path)

    arr = np.genfromtxt(path, dtype=dtype, delimiter=",", skip_header=1)

    return arr
