import numpy as np
path = "data/ipl_matches_small.csv"
dtype = '|S50'
# Enter code here
def read_ipl_data_csv(pathr, dtype="|S50"):
    ipl_matches_array = np.genfromtxt(pathr, delimiter = ',',dtype = dtype, skip_header = 1)

    return ipl_matches_array

print read_ipl_data_csv(path, dtype = '|S50')
