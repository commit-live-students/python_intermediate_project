
import numpy as np
import pandas as pd
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv

def get_unique_teams_set():
    team1 = [] 
    team2 = []
    Total_Teams = []
    mylist = read_ipl_data_csv('data/ipl_matches_small.csv', '|S50')
    np.set_printoptions(threshold=np.nan)
    team1=list(mylist[:,3])
    team2=list(mylist[:,4])
    Total_Teams = set(team1+team2)
    print (Total_Teams)
    return Total_Teams
get_unique_teams_set()



