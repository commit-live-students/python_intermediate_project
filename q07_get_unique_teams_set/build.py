# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = "data/ipl_matches_small.csv"
import numpy as np
# Enter Code Here
# Enter Code Here
def get_unique_teams_set():
    arr=[]

    ipl_matches_array=np.genfromtxt(path,dtype='|S50',skip_header=1,delimiter=",")
    for i in range (len(ipl_matches_array)):
        #print (ipl_matches_array[i])
        arr.append(ipl_matches_array[i][12])
    a=np.unique(arr)
    s=set(a)
    return (s)

get_unique_teams_set()
