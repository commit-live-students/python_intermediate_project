# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
import pandas as pd

def get_total_extras():
    df = pd.read_csv(path)
    count = 0
    for i in range(0,len(df['extras'])):
        count = count + df['extras'][i]
    
    return count
#get_total_extras()


