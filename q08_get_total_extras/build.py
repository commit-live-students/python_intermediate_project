# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import pandas as pd

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    read_ipl_data_csv = np.genfromtxt(path,delimiter=',', dtype=int, skip_header=1)
    extra_runs = read_ipl_data_csv[: , 17]
    extra_runs_sum = np.sum(extra_runs)
    return(int(extra_runs_sum))



