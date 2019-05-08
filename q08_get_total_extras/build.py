# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'


def get_total_extras():
    ipl=read_ipl_data_csv(path,'|S50')
    extras=ipl[:,17].astype(np.int64)
    return np.sum(extras)


get_total_extras().dtype
# Enter Code Here

