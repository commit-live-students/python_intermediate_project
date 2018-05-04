import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_data =  np.genfromtxt(path,dtype='|S20',skip_header=True, delimiter=',')
    single_col = ipl_data[:,1]
    ipl_matches_array = len(np.unique(ipl_data[:,1]))
    return ipl_matches_array


var = get_unique_matches_count()
print(var)


