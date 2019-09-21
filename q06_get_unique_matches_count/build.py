
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
dtype='|S50'

def get_unique_matches_count():
    ipl_matches_array = read_ipl_data_csv(path,dtype)
    return len(set(ipl_matches_array[:, 0]))
get_unique_matches_count()
