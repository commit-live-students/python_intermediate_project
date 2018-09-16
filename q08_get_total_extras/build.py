# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    
    ipl_matches_array=np.genfromtxt(path, dtype=int ,delimiter=',',skip_header=1)
    
    extras=sum(ipl_matches_array[:,17])
    
    return extras


