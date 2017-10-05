# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_total_extras():
    data = read_ipl_data_csv(path,dtype='|S50')
    extras=data[:,17].astype(np.int)
    extras_sum=np.sum(extras)
    return extras_sum



#get_total_extras()
