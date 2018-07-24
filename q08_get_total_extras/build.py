# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
dtype = '|S100'

# Enter Code Here
def get_total_extras():
    arrTotalExtras = np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
    intTotalExtras = arrTotalExtras[:,17].astype(np.int16)
    return intTotalExtras.sum()


