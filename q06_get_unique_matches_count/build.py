# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
#path = 'data/ipl_matches_small.csv'  #path for reference as function should not take any parameter.
import numpy as np

# Enter Code Here
def get_unique_matches_count():  
    
    #loading the file in a variable
    y=np.genfromtxt('data/ipl_matches_small.csv',dtype=None,delimiter=',')
    
    #Getting unique match code ids by using numpy unique function
    #Subtracting 1 from total count as one value among unique cinstitutes for the header
    ipl_matches_array = len(np.unique(y[:,0]))-1  
    return ipl_matches_array
    

get_unique_matches_count()




