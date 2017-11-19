# Default Imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_teams_set():
    count=0
    teams=set()
    data=read_ipl_data_csv(path,"|S50")
    for i in range(0,data.shape[0]):
        if data[i][3] != data[i-1][3]:
            if data[i][3] not in teams:
                teams.add(data[i][3])
        if data[i][4] != data[i-1][4]:
            if data[i][4] not in teams:
                teams.add(data[i][4])
    count=len(teams)

    return count
