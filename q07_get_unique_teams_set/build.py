import numpy as np
import pandas as pd
from numpy import genfromtxt
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = './data/ipl_matches_small.csv'
def get_unique_teams_set():
    def read_ipl_data_csv(file_path, dtype='|S50'):
        ipl_matches_array = np.genfromtxt(file_path,delimiter=',',dtype='|S50',skip_header=1)
        return ipl_matches_array
    teams1 = np.unique(read_ipl_data_csv(path)[:,3])
    teams2 = np.unique(read_ipl_data_csv(path)[:,4])
    teams = set(np.union1d(teams1,teams2))
    return teams
