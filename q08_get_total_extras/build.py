# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import pandas as pd
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    data = pd.read_csv(path,delimiter=',')
    a = data['extras']
    sum1 = a.sum(axis=0)
    extras = int(sum1)
    return extras
get_total_extras()
