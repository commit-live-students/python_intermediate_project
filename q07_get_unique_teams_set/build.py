import numpy as np

from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv


def get_unique_teams_set():
    path = './data/ipl_matches_small.csv'
    ipl_data = read_ipl_data_csv(path,dtype='S50')
    team1Data = np.unique(ipl_data[:,3])
    team2Data = np.unique(ipl_data[:,4])
    resultantArray = np.union1d(team1Data, team2Data)
    resultSet = set(resultantArray)
    return resultSet

testSet = get_unique_teams_set()
print(testSet)

