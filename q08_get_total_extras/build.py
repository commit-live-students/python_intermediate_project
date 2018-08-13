# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    read1 = np.genfromtxt(path,skip_header = 1,delimiter = ",")
    extra1 = read1[:,17]
    extras = int(sum(extra1))
    #print extra1
    #print type(extras)
    return extras

print get_total_extras()
