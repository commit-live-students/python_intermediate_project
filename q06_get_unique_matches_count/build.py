# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    arr = read_ipl_data_csv(path, dtype='|S100')

    _, counts = np.unique(arr[:, 0], return_counts=True)

    Count = len(counts)

    return Count
