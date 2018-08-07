# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    data = read_ipl_data_csv(path, dtype=int)
    ipl_matches_array = int(len(set(data[:,0])))
    return ipl_matches_array

