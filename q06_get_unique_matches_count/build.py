# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'
import numpy as np
import csv
def get_unique_matches_count():
    ipl=[]
 
    with open('data/ipl_matches_small.csv') as csvfile:
        reader=csv.reader(csvfile)
        for x in reader:
            ipl.append(x)
        header=tuple(ipl[0])
        ipl_matches_array= np.unique([x[1] for x in ipl[1:]])    

        match_count=len(ipl_matches_array)
    return match_count
print(get_unique_matches_count())    



