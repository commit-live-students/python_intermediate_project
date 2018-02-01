# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv

path = 'data/ipl_matches_small.csv'


def get_unique_matches_count():

    read1 = np.genfromtxt(path,skip_header = 1,delimiter = ",")

    a =  read1[:,0]
    b = np.unique(a)
    ipl_matches_array = b.size



    return ipl_matches_array


print get_unique_matches_count()
