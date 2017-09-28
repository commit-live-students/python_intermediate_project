import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))

from unittest import TestCase
from q04_read_csv_data_to_ndarray.build import read_csv_data_to_ndarray

class TestRead_ipl_data(TestCase):
    def test_read_ipl_data(self):
        input_dtype = '|S100'
        ipl_array = read_csv_data_to_ndarray("../../data/ipl_matches_small.csv", input_dtype)
        self.assertTrue(ipl_array.shape == (1452, 23))
        self.assertTrue(ipl_array.dtype == input_dtype)