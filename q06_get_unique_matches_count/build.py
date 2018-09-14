# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import pandas as pd
# Enter Code Here
def get_unique_matches_count():
    df=pd.read_csv(path,delimiter=',')
    counts=df['match_code'].nunique()
    return counts
   
    
get_unique_matches_count()


