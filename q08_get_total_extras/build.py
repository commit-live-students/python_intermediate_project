#%load q08_get_total_extras/build.py

import numpy as np

path='./data/ipl_matches_small.csv'

def get_total_extras():
    
    arr=np.genfromtxt(path,delimiter=',',skip_header=1,dtype=int)
#arr
    #print(sum(arr[:,17]))
    ext=sum(arr[:,17])
    return ext

get_total_extras()


