# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_total_extras():
    data = read_ipl_data_csv(path,np.int)
    total =0
    extras= data[:,17]
    for extra in extras:
        total =total+extra
    return total
