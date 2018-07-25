# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    np_ipl_data =  read_ipl_data_csv(path , '|S50')
    #creating tuple for headers
    
    extras = np_ipl_data[:,[17]]
    extras_list = extras.reshape(np.product(extras.shape)).tolist()
    extras_in = [int(x) for x in extras_list]
    return sum(extras_in)

# Enter Code Here


