# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
def get_total_extras():
    ipl = np.genfromtxt(path,delimiter = ',',dtype = int , skip_header= 1)
    extras = []
    for x in ipl:
        extras.append(x[17])
    return sum(extras)


