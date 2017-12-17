import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    ipl_matches_array=[]
    ipl_match=read_ipl_data_csv(path=path,dtype='|S50')
    for matches in ipl_match:
        match_no=matches[0]
        ipl_matches_array.append(match_no)
    cnt=len(set(ipl_matches_array))
    return cnt
