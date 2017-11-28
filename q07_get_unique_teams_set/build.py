# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
import numpy as np
def get_unique_teams_set():
    matches=[]
    for item in np.genfromtxt(path,delimiter=',',dtype='|S50')[1:,3:]:
        for i in range(0,3):
            matches.append(item[i])
    return set(matches)
