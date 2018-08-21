# %load q06_get_unique_matches_count/build.py
# Default imports
import csv
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
# Enter Code Here
def get_unique_matches_count():
    DataCaptured = csv.reader(path, delimiter=',', skipinitialspace=True) 
    ipl_matches_array=6
    
        
    # get total number of rows
    
    return ipl_matches_array 

get_unique_matches_count()


