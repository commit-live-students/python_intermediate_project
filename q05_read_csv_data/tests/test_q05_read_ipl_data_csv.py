import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from q05_read_csv_data.build import read_ipl_data_csv



class TestRead_ipl_data(TestCase):
    def test_read_ipl_data(self):
        ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv', dtype='|S50')
        self.assertTrue(ipl_matches_array.shape == (1451, 23))
        self.assertTrue(ipl_matches_array.dtype == '|S50')
