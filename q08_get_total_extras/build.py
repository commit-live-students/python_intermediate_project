# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = './data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    read_ipl_data_csv = np.genfromtxt(path,dtype=np.int64,delimiter=',',skip_header=1)
    extras = read_ipl_data_csv[:len(read_ipl_data_csv),17:18]
    a = extras.sum()
    return a
