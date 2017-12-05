# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = './data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    a = np.genfromtxt(path,dtype='|S50',skip_header=1,delimiter=',')
    b = a[:len(a),0:1]
#     b = len(ipl_matches_array)
    c = np.unique(b)
    ipl_matches_array = len(c)

    return ipl_matches_array
