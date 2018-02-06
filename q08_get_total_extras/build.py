# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():

    data = read_ipl_data_csv(path,'|S50')
    extras = data[:,17]
    total_extras = 0
    for ele in extras:
        total_extras += int(ele)

    return total_extras
