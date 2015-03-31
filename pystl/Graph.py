from Heap import Heap

def dijkstra(adj, src, path=False):
  """
    implements the dijkstra algorithm for single-source shortest path algorithm
    input:
      adj - the adjacency list, represented as a nested dictionary
            adj[v] = [u_1: E(v, u_1), u_2: E(v, u_2), u_3: E(v, u_3)]
            where E(v, u) is the length of the edge v-u.
  """
  dist = dict()
  pre = dict()
  keys = adj.keys()
  nodes = dict()
  for key in keys:
    dist[key] = float('inf')
  dist[src] = 0
  pre[src] = None
  visited = set()
  visited.add(src)

  # build heap
  heap = Heap(lambda x : dist[x])
  for x in keys:
    if x in visited:
      continue
    node = heap.insert(x)
    nodes[x] = node

  # two basic options
  def extract():
    x = heap.top()
    heap.remove()
    return x

  def tighten(x):
    for y in adj[x].keys():
      if y in visited:
        continue
      if dist[x] + adj[x][y] < dist[y]:
        dist[y] = dist[x] + adj[x][y]
        pre[y] = x
        heap.update(nodes[y])

  # the main algorithm, repeatedly apply extract and tighten.
  tighten(src)
  while heap.size() > 0:
    x = extract()
    visited.add(x)
    tighten(x)

  if path == True:
    return (dist, pre)
  else:
    return dist







