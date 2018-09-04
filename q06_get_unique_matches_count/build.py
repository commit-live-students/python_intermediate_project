from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = './data/ipl_matches_small.csv'
import numpy as np

def get_unique_matches_count():
    arr = np.genfromtxt(path, dtype = '|S50', skip_header=1, delimiter=',')
    arr1 = arr[:,0]
    arr2 = np.unique(arr1)
    var = len(arr2)
    return var





