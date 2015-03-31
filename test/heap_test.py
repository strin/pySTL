import unittest
from pystl.Heap import *

class TestHeap(unittest.TestCase):
  def setUp(self):
    pass

  def test_insert_remmove_all(self):
    heap = Heap()
    for i in range(100):
        heap.insert(random.randint(0, 100))
    for i in range(100):
        heap.remove()
    self.assertEqual(heap.__str__(), "None")

  def test_simple_insert(self):
    heap = Heap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(2)
    self.assertEqual(heap.top(), 1)

if __name__ == "__main__":
  unittest.main()