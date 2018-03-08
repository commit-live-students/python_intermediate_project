# Default imports
import numpy as np

# Enter code here
path = "./data/weather_small_2012.csv"
dtype = '|S50'
def read_ipl_data_csv(path, dtype):
    ipl_matches_array = np.genfromtxt(path, dtype='|S50', skip_header=1, delimiter=",")
    # Enter code here
    return ipl_matches_array

data = read_ipl_data_csv(path, dtype)
print data
