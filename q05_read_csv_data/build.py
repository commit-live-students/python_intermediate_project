# Default imports
import numpy as np
def read_ipl_data_csv(file_path, dtype='|S50'):
    ipl_matches_array = np.genfromtxt(file_path,delimiter=',',dtype='|S50',skip_header=1)
    return ipl_matches_array
