# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
ipl_matches_array = {}
# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = len(read_ipl_data_csv(path,dtype='|S50')[0,0])
    return ipl_matches_array
print get_unique_matches_count()
