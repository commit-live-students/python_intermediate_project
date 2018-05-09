#from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
#path = ''

def get_unique_matches_count():
    arr=np.genfromtxt('./data/ipl_matches_small.csv',delimiter=',',dtype='|S50',skip_header=1)
    ipl_matches_array= np.unique(arr[:,0])
    return len(ipl_matches_array)

get_unique_matches_count()

