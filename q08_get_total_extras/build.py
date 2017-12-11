# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    arr = read_ipl_data_csv(path, dtype='|S100')

    sum_extra = np.array(arr[:, 17:18], dtype=int).sum()
    return sum_extra
