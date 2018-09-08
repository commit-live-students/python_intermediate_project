# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
import pandas as pd
import numpy as np
column_1 = set()
column_2 = set()
def get_unique_teams_set():
    df = pd.read_csv(path)
    '''
    for i in range(0,len(df['match_code'])):
        team1 = df['team1'][i].encode('UTF-8')
        team2 = df['team2'][i].encode('UTF-8')
        if team1 not in column_1:
            column_1.add(team1)
            
        if team2 not in column_2:
            column_2.add(team2)
    '''
    main_arr = read_ipl_data_csv(path,str)
    arr1 = list(np.unique(main_arr[:,3]))
    arr2 = list(np.unique(main_arr[:,4]))
    unique_arr = np.array(np.unique(np.array(arr2+arr1)),dtype=bytes)
    
    return set(unique_arr)
arr = get_unique_teams_set()
type(arr)
#import numpy as np

#arr1
#arr2
#arr2+arr1
#np.array(arr2+arr1)
#np.unique(np.array(arr2+arr1))
#unique_arr = np.unique(np.array(arr2+arr1))



