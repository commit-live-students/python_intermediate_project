# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np
# Enter Code Here
def get_unique_teams_set():

    numpyArr=read_ipl_data_csv(path,dtype='|S50')
    uu1=set(np.unique(numpyArr[:,3]))
    uu2=set(np.unique(numpyArr[:,4]))

    var=uu1 | uu2

    return var


print get_unique_teams_set()    
