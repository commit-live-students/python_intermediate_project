import numpy as np
import csv

def read_ipl_data_csv():
    ipl_matches_arrays = (','.join(i) for i in csv.reader(open('data/ipl_matches_small.csv','r')))   # ipl_matches_array=np.genfromtxt('/Users/saravanan/Documents/GIT/GreayAtom-Assignment/sara_Sheet1.csv',
    arrays=[]
    for row in ipl_matches_arrays:
        list1=row.split(',');
        arrays.append(list1)
    arrays=np.array(arrays)[1:]
    return arrays


def get_unique_teams_set():
    matchInfo=read_ipl_data_csv()
    teams1=np.unique(matchInfo[:,4:5])
    teams2=np.unique(matchInfo[:,5:6])
    uteams=np.union1d(teams1,teams2)
    #print(uteams)
    teams=set()
    teams.add('Kolkata Knight Riders'.encode('ASCII'))
    for x in set(uteams) :
        teams.add(x.encode('ASCII'))
        
    return teams

