# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    extras = np.genfromtxt(path, dtype=None, delimiter=',', skip_header=1,usecols=(17)) #read csv file
    return extras.sum()

