# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    
    matches = np.genfromtxt(path, dtype = np.float64,skip_header = 1, delimiter = ',')
    #matches[]
    
    #np.set_printoptions(threshold = np.nan)
    count = 0
    
    for number in matches[:,17]:
        count = count + number
        
    return count

get_total_extras()



