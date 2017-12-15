import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from q07_get_unique_teams_set.build import get_unique_teams_set

class TestGet_unique_teams_set(TestCase):
    def test_get_unique_teams_set_return(self):
        teams = get_unique_teams_set()
        actual = {'Chennai Super Kings', 'Deccan Chargers', 'Kings XI Punjab', 'Kolkata Knight Riders',
                  'Mumbai Indians', 'Pune Warriors', 'Rajasthan Royals'}
        self.assertTrue(teams == actual,"The Expected teams do not match the actual teams")
