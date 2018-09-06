# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    read = np.genfromtxt(path,delimiter=',',skip_header=1)
    extras= sum(read[:,17])
    return extras
print(get_total_extras())


