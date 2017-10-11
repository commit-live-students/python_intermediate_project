# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    arr=[]
    sum=0
    ipl_matches_array=np.genfromtxt(path,dtype='|S50',skip_header=1,delimiter=",")
    for i in range (len(ipl_matches_array)):
        #print (ipl_matches_array[i])
        sum=sum+int((ipl_matches_array[i][17]))
    return sum


get_total_extras()
