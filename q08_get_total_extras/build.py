
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

# Write your code here
import numpy as np
path = 'data/ipl_matches_small.csv'

def get_total_extras():
    ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv', dtype='|S50')
    extras = ipl_matches_array[:, 17]
    extras_int = extras.astype(np.int16)
    return extras_int.sum()

