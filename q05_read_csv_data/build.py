# Default imports
import numpy as np

def read_ipl_data_csv(path,dtype):
    ipl_matches_array = np.genfromtxt(path, dtype='|S50', skip_header=1, delimiter=',')
    print ipl_matches_array
