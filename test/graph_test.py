from Graph import *
import unittest

class TestDijkstra(unittest.TestCase):
  def test_chain(me):
    src = 1
    adj = {1:{2:1}, 2:{3:2}, 3:{4:3}, 4:{}}
    me.assertEqual(dijkstra(adj, src), {1:0, 2:1, 3:3, 4:6})

  def test_square(me):
    src = 1
    adj = {1:{2:10, 3:3}, 2:{1:10, 4:2, 3:9}, 3:{1:3, 2:9, 4:10}, 4:{2:2, 3:10}}
    me.assertEqual(dijkstra(adj, src), {1: 0, 2: 10, 3: 3, 4: 12})

if __name__ == "__main__":
  unittest.main()