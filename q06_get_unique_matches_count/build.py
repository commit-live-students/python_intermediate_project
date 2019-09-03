# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "./data/ipl_matches_small.csv"
import numpy as np
# Enter Code Here
def get_unique_matches_count():
    ipl_matches_arrayx = np.unique(read_ipl_data_csv(path,dtype=('|S50'))[:,0],return_counts=True)
    ipl_matches_arrayx1 = len(ipl_matches_arrayx[0])
    return ipl_matches_arrayx1
