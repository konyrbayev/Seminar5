from mygraph import Graph
from myalgorithm import dijkstra

f=open('graph_27.txt','r')
line = f.readline()
mymatrix = []
weights = []
graph = Graph()
new_graph = {}
count=0
for line in f:
  mymatrix.append([int(x) for x in line.split()])
  graph.add_vertex(count)
  new_graph[count] = {}
  count += 1

for i in range(len(mymatrix)):
  weights.append(mymatrix[i][len(mymatrix[i]) - 1])



for j in range(len(mymatrix)):
  col = 0
  row = 0
  counter = 0
  for i in range(len(mymatrix[0]) - 1):
    if counter == 0 and mymatrix[j][i] == 1:
      col = i
      counter = 1
      continue
    if mymatrix[j][i] == 1 and counter == 1:
      row = i
      counter = 2
    if counter == 2:
      graph.add_edge(col, row)
      new_graph[col][row] = weights[j]

print('Number of edges: ', graph.num_edges())
print('Number of vertices: ', graph.num_vertices())
print('Minimum path from 1 to 4 is: ', dijkstra(new_graph, 1))
