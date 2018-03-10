# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import pandas as pd
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    df = pd.read_csv(path)
    ipl_matches_array = len(pd.unique(df['match_code']))
    return ipl_matches_array

get_unique_matches_count()
