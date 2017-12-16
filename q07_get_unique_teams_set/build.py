# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import pandas as pd
path = "data/ipl_matches_small.csv"

# Enter Code Here
def get_unique_matches_count(path):
    ipl_matches_array = pd.read_csv(path)
    count = ipl_matches_array.groupby('match_code').size()
    ipl_matches_array = count.count()
    return ipl_matches_array
