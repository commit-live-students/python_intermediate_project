# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here

import numpy as np
import pandas as pd

# Enter Code Here
def get_unique_matches_count():
    path = 'data/ipl_matches_small.csv'
    data = np.genfromtxt(path, delimiter=',',dtype='|S50')
    df = pd.DataFrame(data)
    unar = df[0].unique()
    unar = np.delete(unar,0,0)
    ipl_matches_array = np.count_nonzero(unar)
    return ipl_matches_array
