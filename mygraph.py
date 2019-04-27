from collections import defaultdict
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_vertex(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)

  def num_edges(self):
    return len(self.edges)

  def num_vertices(self):
    return len(self.nodes)

  def get_vertex(self, v):
    if v in self.nodes:
      return self.nodes

  def get_edge(self, u, v):
      if u in self.nodes or v in self.nodes[u]:
        exists = print ("exists")
      else:
        print ("No edge")

  def vertices(self):
    for k in self.nodes():
      return list(self.nodes[k])


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path
