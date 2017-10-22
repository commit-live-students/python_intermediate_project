# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    data = read_ipl_data_csv(path,'|S50')
    extra_runs = data[:,17:18]
    total_extra = np.array(extra_runs).astype(np.int)
    return total_extra.sum()

print get_total_extras()
