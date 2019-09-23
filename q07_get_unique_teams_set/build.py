# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np
def get_unique_teams_set():
        ipl_matches_array=read_ipl_data_csv(path=path,dtype='S50')
        return set(np.unique(ipl_matches_array[:,3:5]))
