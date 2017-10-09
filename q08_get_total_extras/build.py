# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():
    #ipl_matches_array = np.genfromtxt(path,dtype='|S50',delimiter=',',skip_header = 0)
    total = 0
    df = read_ipl_data_csv(path,'|S50')
    for item in df:
        total += int(item[17])

    return total
