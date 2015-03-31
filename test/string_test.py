import unittest
from pystl.string import *

class StringTest(unittest.TestCase):
  def setUp(self):
    pass

  def test_robin_karp(self):
    data = [("why hello_word", "hello"), 
            ("oh my god", "god"), 
            ("fill the tank", "thetank")]
    for (src, pattern) in data:
      self.assertEqual(src.find(pattern), robin_karp(src, pattern))

if __name__ == "__main__":
  unittest.main()
