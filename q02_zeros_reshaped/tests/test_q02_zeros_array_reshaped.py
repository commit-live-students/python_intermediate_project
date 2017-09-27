import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))
from unittest import TestCase
from q02_zeros_reshaped.build import zeros_array_reshaped
from q01_zeros_array.build import zeros_array

class TestZeros_array_reshaped(TestCase):
    def test_zeros_array_reshaped(self):
        var = zeros_array_reshaped()
        self.assertTrue(var.shape == (2,3,4))
