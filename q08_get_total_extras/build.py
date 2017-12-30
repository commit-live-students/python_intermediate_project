import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_total_extras():
    ipl_matches_array = read_ipl_data_csv(path,int)
    extras = sum(ipl_matches_array[:,17])
    return extras

get_total_extras()
