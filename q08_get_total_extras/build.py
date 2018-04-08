# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'
dtype='|S20'
# Enter Code Here
def get_total_extras():
    data=np.genfromtxt(path, skip_header=1,delimiter=",",dtype=dtype);
    x=data[:,17].astype(np.int)
    extrun = np.sum(x)
    return extrun
