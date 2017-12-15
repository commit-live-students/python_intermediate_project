import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from inspect import getargspec
from unittest import TestCase
import numpy as np
from q04_read_csv_data_to_ndarray.build import read_csv_data_to_ndarray
input_dtype = '|S100'
ipl_array = read_csv_data_to_ndarray("data/ipl_matches_small.csv", input_dtype)
class TestRead_ipl_data(TestCase):
    def test_read_ipl_data_arguments(self):
        args = getargspec(read_csv_data_to_ndarray)
        self.assertEqual(len(args[0]),2,"Expected number of arguments does not match the arguments in the solution")

    def test_read_ipl_data_return_shape(self):
        self.assertTrue(ipl_array.shape == (1451, 23),"The Expected shape does not match the returned shape")

    def test_read_ipl_data_return_type(self):
        self.assertTrue(ipl_array.dtype == input_dtype,"The Expected dtype does not match the returned dtype")
