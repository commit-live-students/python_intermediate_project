# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    extra = np.genfromtxt(path, delimiter = ',', dtype = 'str',skip_header = 1)
    extra = extra[:, 17:18]
    #extra = np.sum(extra)
    #extra = np.astype(np.int)
    extra = extra.astype(np.int)
    extra1 = np.sum(extra)
    return (extra1)
print get_total_extras()
