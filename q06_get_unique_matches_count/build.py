# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import pandas as pd

# Enter Code Here
def get_unique_matches_count():
    ipl_matches_array = pd.DataFrame(read_ipl_data_csv('data/ipl_matches_small.csv','|S100')[:,0])[0].nunique()
    return ipl_matches_array



