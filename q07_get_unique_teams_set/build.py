# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "./data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    read_ipl_data_csv = np.genfromtxt(path,dtype='|S50',delimiter=',',skip_header=1)
    team1 = read_ipl_data_csv[:len(read_ipl_data_csv),3:4]
    team2 = read_ipl_data_csv[:len(read_ipl_data_csv),4:5]
    a = np.unique(team1)
    b = np.unique(team2)
    sa = set(a)
    sb = set(b)
    c = sa | sb
    return c
