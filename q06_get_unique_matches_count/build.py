# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
# Enter Code Here
def get_unique_matches_count():
    data = read_ipl_data_csv(path,'|S50')
    return len(np.unique(data[:,0]))

print get_unique_matches_count()


#print get_unique_matches_count(path,'|S50'):
