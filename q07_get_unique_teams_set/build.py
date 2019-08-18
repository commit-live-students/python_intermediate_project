import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path,'|S50')
    t1= set(np.unique(ipl_matches_array[:,3]))
    t2= set(np.unique(ipl_matches_array[:,4]))
    t=t1.union(t2)
    return t

a= get_unique_teams_set()
print a
    
