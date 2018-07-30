# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    data = read_ipl_data_csv(path, dtype='|S50')
    match_count = set()
    for row in data:
        match_count.add(row[0])
    print(len(match_count))
    return len(match_count)
# Enter Code Here
get_unique_matches_count()

