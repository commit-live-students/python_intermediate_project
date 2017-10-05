# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np


path = 'data/ipl_matches_small.csv'

def get_total_extras():
    ipl = np.genfromtxt(path,delimiter=',',dtype='|S50')[:,-6]
    ipl_matches_array = read_ipl_data_csv(path,'|S50')
    return sum(ipl_matches_array[:,-6].astype(int))

# Enter Code Here
