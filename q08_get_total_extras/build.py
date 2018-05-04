# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    weather = np.genfromtxt(path,dtype='|S20',skip_header=True, delimiter=',')
    return weather[:,17].astype(int).sum()
get_total_extras()


