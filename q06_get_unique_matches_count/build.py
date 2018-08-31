# %load q06_get_unique_matches_count/build.py
# Default imports
import numpy as np
import pandas as pd
path = 'data/ipl_matches_small.csv'
dtype = float

def get_unique_matches_count():
    ipl_matches = pd.read_csv(path)
    ipl_matches_array = ipl_matches['match_code'].nunique()
    return ipl_matches_array         
    
          
        
    


