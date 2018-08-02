# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
data= np.genfromtxt(path, dtype='float', delimiter= ',', skip_header=1)
# Enter Code Here

def get_total_extras():
    extras_column = data[:,17]
    extras= int(np.sum(extras_column))
    return extras




