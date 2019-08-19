# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_matches_array=read_ipl_data_csv(path,np.float64)
    #len(np.unique(ipl_matches_array[0:,0]))
    return (int(np.sum(ipl_matches_array[0:,17])))
    #return unique_matches_count

    #print np.array([unique_elements,freq]).T
get_total_extras()
