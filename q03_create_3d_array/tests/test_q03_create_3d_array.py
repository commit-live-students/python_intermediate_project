import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

import numpy as np

from unittest import TestCase
from q03_create_3d_array.build import create_3d_array

actual = [
            [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]],

            [[9, 10, 11],
             [12, 13, 14],
             [15, 16, 17]],

            [[18, 19, 20],
             [21, 22, 23],
             [24, 25, 26]]
        ]
arr = create_3d_array()

class TestCreate_3d_array(TestCase):
    def test_create_3d_array_return_value(self):
        

        self.assertTrue(np.all(arr == actual),"The Expected array does not match returned array")
