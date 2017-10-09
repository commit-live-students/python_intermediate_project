# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_matches_array = np.genfromtxt(path,dtype='|S50',skip_header=1, delimiter=",")
    res = ipl_matches_array[:,-6].astype(np.float16)
    return res.sum()

get_total_extras()
