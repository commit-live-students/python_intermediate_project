from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = './data/ipl_matches_small.csv'
import numpy as np

def get_unique_teams_set():
    arr = np.genfromtxt(path, dtype = '|S50', skip_header=1, delimiter=',')
    arr1 = arr[:,3]
    arr2 = arr[:,4]
    arr3 = np.unique(arr1)
    arr4 = np.unique(arr2)
    
    read_unique = list(np.union1d(arr3, arr4))
    
    return read_unique
    
    

from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = './data/ipl_matches_small.csv'
import numpy as np

arr = np.genfromtxt(path, dtype = '|S50', skip_header=1, delimiter=',')
arr1 = arr[:,3]
arr2 = arr[:,4]
arr3 = np.unique(arr1)
arr4 = np.unique(arr2)

def get_unique_teams_set():
    read_unique1 = set(np.union1d(arr3, arr4))
    print(read_unique1)
    
    return read_unique1

get_unique_teams_set()


