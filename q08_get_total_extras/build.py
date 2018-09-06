from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = './data/ipl_matches_small.csv'

def get_total_extras():
    path = './data/ipl_matches_small.csv'
    arr = np.genfromtxt(path, dtype = 'int', skip_header=1, delimiter=',')
    total = sum(arr[:,17])
    
    return total
    





