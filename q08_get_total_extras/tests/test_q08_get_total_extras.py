import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from q08_get_total_extras.build import get_total_extras
from unittest import TestCase


class TestGet_total_extras(TestCase):
    def test_get_total_extras_return_values(self):
        runs = get_total_extras()
        self.assertTrue(runs == 88,"The Expected value does not match return value")

