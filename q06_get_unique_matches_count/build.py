# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    df = read_ipl_data_csv(path,'|S50')
    temp = set()
    for item in df:
        temp.add(item[0])
    count = len(temp)
    return count
