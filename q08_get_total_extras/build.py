# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    data = read_ipl_data_csv(path,dtype=np.int16)
    extras=data[:len(data),17:18]
    sum1 = extras.sum()


    return sum1
print get_total_extras()
