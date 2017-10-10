# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    ipl_matches_array = np.genfromtxt(path,dtype='|S50', skip_header=1,delimiter = ',')
    extras = ipl_matches_array[:,17].astype(np.int)
    Sum = extras.sum()
    return Sum

get_total_extras()
