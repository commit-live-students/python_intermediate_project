# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():
    a = read_ipl_data_csv(path,dtype = '|S50')
    b = np.array([]).astype(np.float)
    for i in a:
        b = np.append(b,i[17])
        b = b.astype(np.int)

        Sum = np.sum(b)
    return Sum 
