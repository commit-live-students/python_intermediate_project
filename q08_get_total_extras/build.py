# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    extra=0
    for item in np.genfromtxt(path,delimiter=',',dtype='|S50')[1:,17:18]:
        extra += int(item[0])
    return extra
