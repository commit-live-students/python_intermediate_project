# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
# Enter Code Here
def get_total_extras():
    ipl = np.genfromtxt(path,skip_header=1,delimiter=',')
    extras = ipl[:,17].astype(np.int32)
    sumex = np.sum(extras)
    return sumex
get_total_extras()

