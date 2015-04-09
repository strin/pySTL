import unittest
from pystl.Sort import *
import random

class SortTest(unittest.TestCase):
  def test_shell_sort(self):
    rnd = random.Random()
    n = 1000
    data = map(lambda x : rnd.randint(0,n), range(n))
    truth = sorted(data)
    result = shell_sort(data)
    self.assertEqual(truth, result)
