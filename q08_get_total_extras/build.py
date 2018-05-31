import numpy as np

from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv


def get_total_extras():
    path = './data/ipl_matches_small.csv'
    
    ipl_data = read_ipl_data_csv(path,dtype='int')

    extraRuns = np.sum(ipl_data[:,17])

    return extraRuns
    
runs = get_total_extras()
print(runs)

