from Heap import Heap

def dijkstra(adj, src, path=False):
  """
    implements the dijkstra algorithm for single-source shortest path algorithm
    input:
      adj - the adjacency list, represented as a nested dictionary
            adj[v] = [u_1: E(v, u_1), u_2: E(v, u_2), u_3: E(v, u_3)]
            where E(v, u) is the length of the edge v-u.
      src - the source node.
      path - if output shortest paths as second output result
    output:
      if path is False:
        return a *dist* of type dictionary, dist[v] stores distance from src to v.
      otherwise:
        return (dist, pre), where pre[v] stores the preceding node in path.
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

def floyd_warshall(adj):
  """ implements the floyd_warshall algorithm
  input:
    adj - the adjacency list, represented as a nested dictionary
            adj[v] = [u_1: E(v, u_1), u_2: E(v, u_2), u_3: E(v, u_3)]
            where E(v, u) is the length of the edge v-u.
  return:
    *dist[u][v]* of type nested dictionary.
  """
  dist = dict()
  keys = adj.keys()
  for x in keys:
    dist[x] = dict()
    dist[x][x] = 0
    for y in keys:
      if y != x:
        dist[x][y] = float('inf')
  for x in keys:
    if not adj.has_key(x):
      continue
    for y in adj[x]:
      dist[x][y] = adj[x][y]
  for k in keys:
    for x in keys:
      for y in keys:
        if dist[x][k] + dist[k][y] < dist[x][y]:
          dist[x][y] = dist[x][k] + dist[k][y]
  return dist
  

