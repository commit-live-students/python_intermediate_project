# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'
iplrecord=read_ipl_data_csv(path,dtype='|S50')

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array=np.unique(iplrecord[:,0]).shape[0]
    return ipl_matches_array
