# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
def get_unique_matches_count():
    a=read_ipl_data_csv(path,dtype='|S50')
    b=np.unique(a[:,[0]])
    return np.count_nonzero(b)
