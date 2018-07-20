# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'


# read the file first column, set to get unique and count the length
def get_unique_matches_count():
    ipl_matches_array = len((set(list(read_ipl_data_csv(path,'int32')[:,0]))))
    return ipl_matches_array

get_unique_matches_count()



