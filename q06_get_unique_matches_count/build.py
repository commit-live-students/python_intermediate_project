# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    #print(np.version.version)
    ipl_matches_array = read_ipl_data_csv(path,dtype='|S50')
    #print(ipl_matches_array.shape)
    #print(type(ipl_matches_array))
    #unique, counts = np.unique(ipl_matches_array[:,[0]], return_counts = True)
    #print(counts)
    test = np.unique(ipl_matches_array[:,[0]])
    #print(test.size)
    return int(test.size)

    #test = np.unique(ipl_matches_array, axis=0)
    #count = np.unique(ipl_matches_array)
#get_unique_matches_count()
