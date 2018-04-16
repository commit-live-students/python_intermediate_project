# %load q07_get_unique_teams_set/build.py
# Default imports
import numpy as np
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_unique_teams_set():
    data = read_ipl_data_csv(path, dtype='|S50')
    team1 = set(data[:,3])
    team2 = set(data[:,4])
    return team1.union(team2)


d = get_unique_teams_set()
d
from unittest import TestCase
class T(TestCase):
    def test_get_unique_teams_set_return(self):
        teams = get_unique_teams_set()
        actual = {b'Deccan Chargers', b'Kings XI Punjab', b'Chennai Super Kings', b'Mumbai Indians',
                  b'Rajasthan Royals', b'Pune Warriors', b'Kolkata Knight Riders'}
        self.assertEqual(teams, actual, 'The Expected teams do not match the actual teams')
t = T()
t.test_get_unique_teams_set_return()


