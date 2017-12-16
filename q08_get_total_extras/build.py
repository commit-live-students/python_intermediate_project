# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():

    data = read_ipl_data_csv(path, dtype='|S50')
    extra = data[:,17].astype(np.int16)
    extras = extra.sum(axis=0)
    #print extras
    #print data

    return extras
