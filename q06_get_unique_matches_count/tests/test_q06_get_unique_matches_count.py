import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase

from q06_get_unique_matches_count.build import get_unique_matches_count


class TestGet_unique_matches_count(TestCase):
    def test_get_unique_matches_count(self):
        matches_count = get_unique_matches_count()
        self.assertTrue(matches_count == 6,"The Expected count does not match the return count")

