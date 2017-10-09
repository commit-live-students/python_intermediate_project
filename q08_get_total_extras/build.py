# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
def get_total_extras():
    ipl_matches_array = read_ipl_data_csv(path, "|S50")
    extraarray = ipl_matches_array[:,17]
    #print(extraarray)
    x = extraarray.astype(int)
    s = np.sum(x)
    return s


# Enter Code Here
