# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    count=0
    data=read_ipl_data_csv(path,"|S50")
    for i in range(0,data.shape[0]):
        if data[i][2] != data[i-1][2]:
            count+=1

    return count
