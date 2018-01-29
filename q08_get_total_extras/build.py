# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    numpyArr = read_ipl_data_csv( path , dtype='|S50' )
    numpyArr1 = numpyArr[:,17]
    extras=numpyArr1.astype(int).sum()

    return extras


print get_total_extras()
