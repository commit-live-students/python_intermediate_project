import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_match_array=read_ipl_data_csv(path,'|S50')
    test=np.unique(ipl_match_array[:,0])
    get_unique_matches_count=np.size(np.unique(ipl_match_array[:,0]))
    return get_unique_matches_count
