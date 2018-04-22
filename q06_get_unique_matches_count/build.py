# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

def get_unique_matches_count():
    temp=[]
    ipl_data=np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    print(np.unique(ipl_data[0][0]))
    for i in ipl_data:
        #print((str(i[0])))
        temp.append(str(i[0]))
    return(len(np.unique(temp)))
    #ipl_matches_array=
# Enter Code Here


