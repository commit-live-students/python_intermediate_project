# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np

def get_unique_matches_count():
    #count = 0
    f1 = read_ipl_data_csv(path,dtype='|S50')
    #print type(f1)
    ipl_matches_array = np.unique(f1[:,0],return_counts=True)
    #print type(ipl_matches_array)

    return ipl_matches_array


print get_unique_matches_count()
