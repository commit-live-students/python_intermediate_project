import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))
from unittest import TestCase
from q01_zeros_array.build import array_zeros

class TestZeros_array(TestCase):
    def test_zeros_array(self):
        var = array_zeros()
        self.assertTrue(var.shape==(3,4,2))
        self.assertTrue(var.max()==0)