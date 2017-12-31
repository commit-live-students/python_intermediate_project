# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array=read_ipl_data_csv(path,np.float64)
    #unique_elements,count_elements= np.unique(ipl_matches_array,return_counts=True)
    #np.count_nonzero(ipl_matches_array=='match_code')
    #unique_elements,count_elements== np.unique(ipl_matches_array,return_counts=True)
    #np.count_nonzero(unique_elements=='match_code')
    #freq=np.bincount(count_elements)
    #print freq
    #print unique_elements,count_elements
    #print unique_elements[0]
    #print count_elements[3]

    unique_matches_count=len(np.unique(ipl_matches_array[0:,0]))
    #print np.unique(ipl_matches_array[0:,0])
    return unique_matches_count

    #print np.array([unique_elements,freq]).T
get_unique_matches_count()
