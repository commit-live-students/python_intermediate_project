# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

# Enter Code Here
def get_total_extras():
    ipl_matches_array  = np.genfromtxt('./data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=",")
    extras = ipl_matches_array[:,17].astype(np.int).sum()
    return extras
