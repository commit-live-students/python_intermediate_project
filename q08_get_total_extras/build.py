# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_matches_array = read_ipl_data_csv(path,dtype='|S50')
    ipl_matches_array = ipl_matches_array[:,[17]].astype(np.int8)
    #print(ipl_matches_array.dtype)
    extras = int(np.sum(ipl_matches_array, dtype = int, axis = 0))
    #print(type(extras))
    return extras
#get_total_extras()
