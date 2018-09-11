# %load q07_get_unique_teams_set/build.py
# Default imports
import pandas as pd
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_teams_set():
    arr1=read_ipl_data_csv()
    team1=arr1[1:,4]
    team2=arr1[1:,3]
    union=np.union1d(team1,team2)
    union1=set(union)
    return union1

def read_ipl_data_csv():
    arr2= np.genfromtxt(path, delimiter=',', dtype='|S50')
    return arr2

get_unique_teams_set()



