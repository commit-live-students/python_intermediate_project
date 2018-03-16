# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'


def get_total_extras():
    data = np.genfromtxt(path,dtype = float, delimiter = ",", skip_header = 1)
    extras = data[:,-6]
    extras_1 = np.sum(extras)
    return int(extras_1)
# Enter Code Here
