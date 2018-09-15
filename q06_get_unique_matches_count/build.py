#%load q06_get_unique_matches_count/build.py

import numpy as np

path='./data/ipl_matches_small.csv'

def get_unique_matches_count():
    
    ipl_matches_array=np.genfromtxt(path,delimiter=',',skip_header=1,dtype='|S20')
#print(ipl_matches_array)

    nouniquecounts=np.unique(ipl_matches_array[:,0],axis=0)
    nocounts=nouniquecounts.size
    

#print(noCounts.size)
    return nocounts





