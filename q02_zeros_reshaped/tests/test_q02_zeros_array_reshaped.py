import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from q02_zeros_reshaped.build import array_reshaped_zeros
from greyatomlib.python_intermediate.q01_zeros_array.build import array_zeros

class TestZeros_array_reshaped(TestCase):
    def test_zeros_array_reshaped_return_shape(self):
        var = array_reshaped_zeros()
        self.assertTrue(var.shape == (2,3,4),"The Expected shape does not match the return shape")
