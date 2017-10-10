# %load q08_get_total_extras/build.py
# Default Imports
#from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
def get_total_extras():
    ipl_matches_array = np.genfromtxt(path,dtype='|S50',delimiter=',')
# Enter Code Here
#np.unique(ipl_matches_array[1:1451,17])
    get_total_extras=np.sum(ipl_matches_array[1:1452,17].astype(np.float),dtype = np.int,axis = None)
    return get_total_extras
