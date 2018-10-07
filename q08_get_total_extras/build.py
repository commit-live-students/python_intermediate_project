# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = './data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    array1=np.genfromtxt(path,delimiter=',')
    result=np.sum(array1[:,17][~np.isnan(array1[:,17])])
    return(np.int64(result))
get_total_extras()

