# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import numpy as np
import csv

def get_unique_matches_count():
    
    no_of_matches_played = 0
    with open(path,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        data = [row for row in csvreader] 
        np_ipl_data = np.asarray(data)

    headers = tuple(np_ipl_data[0])
    
    #slicing main ndarray into required ndarray
    match_codes = np_ipl_data[1:,[headers.index('match_code')]]
    
    #reshaping ndarray from 2d to 1d to make a list
    match_codes_array = match_codes.reshape(np.product(match_codes.shape))
    
    #converting 1d array to a list and then removing duplicates to get unique values
    match_codes_set = set(match_codes_array.tolist())
    
    #length of the set will be the total number of matches played
    no_of_matches_played = len(match_codes_set)
    return no_of_matches_played


