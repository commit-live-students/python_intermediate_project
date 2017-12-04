import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Define function get_unique_matches_count and pass the loaded array to read each element
# and fetch the first element (Match Code). Once all the element[0] are extracted and loaded
# in new numpy array get_unique_id, execute a unique numpy function to return unique match codes
# and then get the count using in built size function
get_unique_id=[]
def get_unique_matches_count():
    #Call the function read_ipl_data_csv to load the file into numpy array-2D
    get_array = read_ipl_data_csv(path, "|S50")

    for element in get_array:
        get_unique_id.append(element[0])

    Count_val = np.unique(get_unique_id, return_index=False, return_counts=True)[0]
    Count = np.size(Count_val)
    return Count
