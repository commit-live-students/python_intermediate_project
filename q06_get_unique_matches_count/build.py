# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

import numpy as np

# Enter Code Here
def get_unique_matches_count():
    matches=[]
    for item in np.genfromtxt(path,delimiter=',',dtype='|S50')[1:,0:1]:
        matches.append(item[0])
    return len(set(matches))
