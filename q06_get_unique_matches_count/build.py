# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import pandas as pd
# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = pd.read_csv(path)
    count = ipl_matches_array.groupby('match_code').size()
    ipl_matches_array = count.count()
    return ipl_matches_array
