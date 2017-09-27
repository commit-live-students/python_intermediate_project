import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))
from unittest import TestCase
from q01_zeros_array.build import zeros_array

class TestZeros_array(TestCase):
    def test_zeros_array(self):
        var = zeros_array()
        self.assertTrue(var.shape==(3,4,2))
        self.assertTrue(var.max()==0)