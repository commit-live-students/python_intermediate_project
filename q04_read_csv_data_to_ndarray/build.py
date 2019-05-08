# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# match_code,date,city,team1,team2,toss_winner,toss_decision,winner,win_type,win_margin,inning,delivery,batting_team,batsman,non_striker,bowler,runs,extras,total,extras_type,player_out,wicket_kind,wicket_fielders

# Enter code here
def read_csv_data_to_ndarray(path, dtype = np.float64 ):
    data = np.genfromtxt(path, dtype, delimiter=',',  skip_header=1)
    return data



