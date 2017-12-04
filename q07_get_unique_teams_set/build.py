import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# In the newly defined function get_unique_teams_set firstly
# Call the read_ipl_data_csv function to load the data into numpy array
# Using for loop create two sets of numpy array for team1 and team2
# Form a Union of above two set to give the final unique set "variable"

set_team1=[]
set_team2=[]

def get_unique_teams_set():
        array_fl = read_ipl_data_csv(path,"|S50")
        for element in array_fl:
            set_team1.append(element[3])
            set_team2.append(element[4])
        variable = set(set_team1) | set(set_team2)
        return variable
