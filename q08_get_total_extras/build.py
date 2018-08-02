# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
import numpy as np
def get_total_extras():
    extras = read_ipl_data_csv(path,'|S50')
    extrasrun =  np.array(extras[:, 17]).astype(np.int32).sum() 
    
    return extrasrun
# Enter Code Here



