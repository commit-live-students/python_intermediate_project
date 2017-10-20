# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path,dtype='|S50')
    a = np.array([])
    for i in ipl_matches_array:
        a = np.append(a,i[0])
        count = (np.unique(a)).size
    return count
