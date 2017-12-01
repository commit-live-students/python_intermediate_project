# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray():
    marks = np.genfromtxt("./data/ipl_matches_small.csv",delimiter=',')
    print marks

read_csv_data_to_ndarray()
