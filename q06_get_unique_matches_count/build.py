# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import pandas as pd
data = pd.read_csv(path)
def get_unique_matches_count():
    m = data['match_code'].nunique()
    return m
    


