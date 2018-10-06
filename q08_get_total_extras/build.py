# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    total_extras=0
    mylist = read_ipl_data_csv(path,int)
    np.set_printoptions(threshold=np.nan)
    total_extras=sum(list(mylist[:, 17]))
    return total_extras
get_total_extras()


