# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    data = read_ipl_data_csv(path,dtype='|S50')
    list_value = []
    for i in data:
        list_value.append(i[0])

    set_value = set(list_value)
    ipl_matches_array = len(set_value)
    return ipl_matches_array

#print get_unique_matches_count()
