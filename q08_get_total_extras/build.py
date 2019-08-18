# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    data = read_ipl_data_csv(path,'|S50')
    extras = data[:,17]
    extras_int = extras.astype(np.int)
    extras_total = np.sum(extras_int)
    return extras_total
