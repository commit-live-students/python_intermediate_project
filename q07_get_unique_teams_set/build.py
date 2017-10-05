from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
def get_unique_teams_set():
    x=read_ipl_data_csv(path,'|S50')
    Count=np.unique(x[:,[3,4]])
    return set(Count)
