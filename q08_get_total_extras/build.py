# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    extras=0
    ipl_match=read_ipl_data_csv(path=path,dtype='|S50')
    for matches in ipl_match:
        extras=extras+int(matches[17])
    return extras
