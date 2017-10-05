# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_matches_count():
    data = read_ipl_data_csv(path,dtype='|S50')
    match_codes=data[:,0]
    unique_code, counts_fre_code=np.unique(match_codes,return_counts=True)
    count=unique_code.size
    return count
#temp =get_unique_matches_count()
#match_code =temp[:,0]
#unique_elements, counts_elements=np.unique(match_code,return_counts=True)

#unique_elements.size
#get_unique_matches_count()
