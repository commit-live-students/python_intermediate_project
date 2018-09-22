# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_matches_count():
    varfile=np.genfromtxt(path,dtype='|S20',delimiter=',',skip_header=1,)
    varcol=varfile[:,0]
    ipl_matches_array = np.count_nonzero(np.unique(varcol))
    return ipl_matches_array
varfile=np.genfromtxt(path,dtype='|S20',delimiter=',',skip_header=1,)
get_unique_matches_count()
import numpy as np
path = 'data/ipl_matches_small.csv'
varfile
#for i in varfile: print(i[1],i[2])
#np.unique(varfile[0])
#varfile[0]
#ipl_ctr=np.ndarray(shape=(1,0), dtype=float, order='F')
varcol=varfile[:,0]

np.unique(varcol)


