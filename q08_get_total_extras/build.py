# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_array = np.genfromtxt(fname=path,delimiter=',',dtype='|S100',skip_header=1)
    ipl_extras = ipl_array[:,17].astype(np.int)
    ipl_extras_count = 0
    ipl_extras_count = int(ipl_extras.sum())
    print(type(ipl_extras_count))
    return ipl_extras_count
get_total_extras()


