# %load q06_get_unique_matches_count/build.py
# Default imports
import pandas as pd
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
ipl_df=pd.read_csv(path)

def get_unique_matches_count():
    ipl_matches_array =ipl_df['match_code'].unique()
    return len(ipl_matches_array)
type(get_unique_matches_count())


