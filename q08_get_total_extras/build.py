# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    narray = read_ipl_data_csv(path, '|S50')
    extras = np.array(narray[:, 17], dtype=np.int)
    #print extras
    return extras.sum(axis=0)

#get_total_extras()
