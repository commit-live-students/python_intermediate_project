# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    ipl_matches = read_ipl_data_csv(path,'|S50')
    extras = sum(ipl_matches[:,17].astype(np.int16))
    return extras;
