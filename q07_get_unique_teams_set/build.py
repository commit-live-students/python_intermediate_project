# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_teams_set():
    data = read_ipl_data_csv(path,'|S50')
    b= np.unique(data[:,3:5])
    a =set(b)
    return a
