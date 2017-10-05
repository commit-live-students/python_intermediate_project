
import pprint
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
s = set()
# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array  = np.genfromtxt('./data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=",")
    matchcodes = ipl_matches_array[1:-1,0]
    for val in matchcodes:
        s.add(val)
    return len(s)
