# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import csv

path = 'data/ipl_matches_small.csv'
def get_total_extras():
    l=[]
    l=np.genfromtxt(path,delimiter=',')
    a=(np.sum(l[1:,17]))
    a=int(a)
    return (a)

    # Enter Code Here

