# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    
    np_ipl_data = read_ipl_data_csv(path , '|S50')
    #creating tuple for headers
    headers = tuple(np_ipl_data[0])
    
    #team 1 2d array
    team_1 = np_ipl_data[1:,[headers.index('team1')]]
    
    #reshaping to 1d array
    team_1_1d = team_1.reshape(np.product(team_1.shape))
    
    #team 1 2d array
    team_2 = np_ipl_data[1:,[headers.index('team2')]]
     
    #reshaping to 1d array
    team_2_1d = team_2.reshape(np.product(team_2.shape))
    
    #taking union of two lists to remove duplicates and merge two lists in one list
    names_of_teames_played = set().union(team_1_1d,team_2_1d)
    
    return names_of_teames_played



