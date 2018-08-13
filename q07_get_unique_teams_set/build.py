# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"


# Enter Code Here
def get_unique_teams_set():

    read1 = read_ipl_data_csv(path,'|S50')
    team1 =  read1[:,3]
    team2 = read1[:,4]

    team11 = set(team1)
    team22 = set(team2)

    #print type(team11)
    #print type(team22)

    union = team11 | team22


    #print team11
    #print team22
    return union
    #return read1


print get_unique_teams_set()
