# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_matches_array = np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    extra_runs_array = ipl_matches_array[0:,17].astype(np.int16)
    sum_of_runs = extra_runs_array.sum()
    return sum_of_runs
print get_total_extras()
