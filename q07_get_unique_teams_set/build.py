# %load q07_get_unique_teams_set/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

#===
path = './data/ipl_matches_small.csv'
dtype = '|S50'

#def read_ipl_data_csv(path, dtype = '|S50'):
 #   ipl_matches_array = np.genfromtxt(path,dtype,delimiter=',', skip_header=1)
  #  return ipl_matches_array

#read_ipl_data_csv(path, dtype)

#===
# Enter Code Here
#import csv
def get_unique_teams_set():
    ipl = []
    ipl = read_ipl_data_csv(path,dtype)
    
    #with open('data/ipl_matches_small.csv') as csvfile:
     #   reader = csv.reader(csvfile)
      #  for x in reader:
       #     ipl.append(x)
        
    team1 = [x[3] for x in ipl[1:]]
    team2 = [x[4] for x in ipl[1:]]
    
    team1 = set(team1)
    team2 = set(team2)
    teams = team1.union(team2)
    #print(teams)
    return teams

get_unique_teams_set()


