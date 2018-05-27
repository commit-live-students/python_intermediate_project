import numpy as np

def get_unique_matches_count():
    
    path = './data/ipl_matches_small.csv'
    ipl_matches = np.genfromtxt(path,delimiter=',',dtype=int, 
                                 usecols=(0), skip_header=1)
    ipl_match_unique = np.unique(ipl_matches,axis=0)
    ipl_matches_array = len(ipl_match_unique)
    return ipl_matches_array
testArray = get_unique_matches_count()
print(testArray)

