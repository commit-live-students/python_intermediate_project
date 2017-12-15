import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from q01_zeros_array.build import array_zeros
var = array_zeros()

class TestZeros_array(TestCase):
    def test_zeros_array_return_shape(self):
        
        self.assertTrue(var.shape==(3,4,2),'Expected Shape does not match return shape')

    def test_zeros_array_return_value_max(self):
        self.assertTrue(var.max()==0,'Expected value does not match return value')