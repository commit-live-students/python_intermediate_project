# Default Imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    data=read_ipl_data_csv(path,'|S50')
    extras=(data[:,17])
    total_extras=int(np.sum(extras.astype(np.int)))
    return total_extras
