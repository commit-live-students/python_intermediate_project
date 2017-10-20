import numpy as np# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

def get_unique_teams_set():
    ipl_matches_array = read_ipl_data_csv(path,dtype = '|S50')
    b = np.array([])

    for i in ipl_matches_array:
        b = np.append(b,i[3])
        b = np.append(b,i[4])

        count = set(b)
    return count
