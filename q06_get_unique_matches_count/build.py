# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path,'|S50')
    match_id=[]

    for i in ipl_matches_array:
        match_id.append(i[0])

    total_matches = np.unique(match_id)
    count = len(total_matches)
    return count

get_unique_matches_count()
