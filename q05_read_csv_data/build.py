# Default imports
import numpy as np

def read_ipl_data_csv():
    ipl_matches_array = np.genfromtxt("./data/ipl_matches_small.csv", dtype='|S50', delimiter=",")
    return ipl_matches_array

read_ipl_data_csv()

# Enter code here
