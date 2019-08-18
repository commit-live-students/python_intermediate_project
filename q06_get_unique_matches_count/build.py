# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    data = read_ipl_data_csv(path,'|S50')
    print data[:,0]
    uniq = (np.unique(data[:,0])).size
    return uniq
