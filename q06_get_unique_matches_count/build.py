import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path,'|S50')
    return np.unique(ipl_matches_array[:,0]).size
#get_unique_matches_count()
