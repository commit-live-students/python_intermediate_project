# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
dtype = '|S50'

# Enter Code Here
my_data = np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
def get_total_extras():
    extras = my_data[:,17].astype(np.int16)
    return sum(extras).astype(np.int16)
        
get_total_extras()

