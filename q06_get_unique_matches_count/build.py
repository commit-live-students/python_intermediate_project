# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    new = read_ipl_data_csv(path,dtype='|S50')
    new_set = set(new[:,0])
    ipl_matches_array = (len(new_set))

    return ipl_matches_array
