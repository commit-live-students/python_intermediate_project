# Default Imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_total_extras():
    extras=0
    data=read_ipl_data_csv(path,"|S50")
    for i in range(0,data.shape[0]):
        extras+=int(data[i][17])

    return extras
