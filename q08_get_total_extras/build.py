# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    def read_ipl_data_csv(file_path, dtype='int64'):
        ipl_matches_array = np.genfromtxt(file_path,delimiter=',',dtype='int64',skip_header=1)
        return ipl_matches_array
    extra_runs_array = read_ipl_data_csv(path)[0:,17]
    sum_of_runs = extra_runs_array.sum()
    return sum_of_runs
