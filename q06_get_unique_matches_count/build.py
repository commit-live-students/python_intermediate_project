# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
import pandas as pd

def get_unique_matches_count():
    df = pd.read_csv(path)
    list1 = []
    for i in range(0,len(df['match_code'])):
        match_code_1 = df['match_code'][i]
        if match_code_1 not in list1:
            list1.append(match_code_1)
    
    return len(list1)





