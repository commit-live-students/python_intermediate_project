# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np

# Enter Code Here
def get_unique_matches_count():
    arr=[]
    a=[]
    ipl_matches_array=np.genfromtxt(path,dtype='|S50',skip_header=1,delimiter=",")
    #print(ipl_matches_array)
    for i in range (len(ipl_matches_array)):
        arr.append(ipl_matches_array[i][0])
    a=np.unique(arr)
    return (len(a))


get_unique_matches_count()
