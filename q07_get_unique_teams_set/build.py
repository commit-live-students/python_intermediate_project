# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv

#Path of the csv file to be passed onto function
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    
    #Loading csv file
    a = read_ipl_data_csv(path,dtype=None)
    
    #creating empty set variables so that same team name doesn't get added repeatedly.
    team1 = set() 
    team2 = set()

    #Looping thru list and getting inside tuple for team name fetching
    for i,v in enumerate(a):
        team1.add(a[i][3])
        team2.add(a[i][4])
    
    #returning union of two
    return team1.union(team2)  # team1|team2 would do as well.

#Call to a function - 
get_unique_teams_set()




