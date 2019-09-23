# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    ipl_data_arr = read_ipl_data_csv(path,'|S50')
    extras =  ipl_data_arr[:,-6]
    return extras.astype(np.int).sum()
#get_total_extras()
