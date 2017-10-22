# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype=np.float64):

    #print path
    #data = np.loadtxt(path,dtype = {'names' : ['match_code','date','city','team1','team2','toss_winner','toss_decision','winner','win_type','win_margin','inning','delivery','batting_team','batsman','non_striker','bowler','runs','extras' , 'total' , 'extras_type' , 'player_out' , 'wicket_kind' , 'wicket_fielders'] , 'formats' : ['S100','M8[D]','S1','S1','S1','S1','S1','S1','S1','i4','i4','f8','S1','S1','S1','S1','i4','i4','i4','S1','S1','S1','S1']},delimiter=',',skiprows=1)

    data = np.genfromtxt(path,dtype=dtype,delimiter=',',skip_header=1)


    return data

read_csv_data_to_ndarray(path,'|S100')
