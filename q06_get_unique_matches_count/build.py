from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = './data/ipl_matches_small.csv'
dtype ='|S50'
import numpy as np
def get_unique_matches_count():
    ipl_matches=np.genfromtxt(path,dtype,skip_header=1,delimiter=',')
    ipl_matches_array=ipl_matches[:,0]
    return len(set(ipl_matches_array))




