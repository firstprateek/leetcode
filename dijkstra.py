from heapq import heapify, heappush, heappop
from collections import defaultdict
from math import inf

def dijkstra(edges, start, end):
  visited = set()
  graph = defaultdict(dict)
  dist = {}
  prev = {}
  for in_vertex, out_vertex, weight in edges:
    graph[in_vertex][out_vertex] = weight
    dist[in_vertex] = inf
    dist[out_vertex] = inf
    prev[in_vertex] = None
    prev[out_vertex] = None

  pq = [ (dist[vertex], vertex) for vertex in graph.keys() ]
  heapify(pq)
  heappush(pq, (0, start))

  while pq:
    topdist, top = heappop(pq)
    if top in visited:
      continue

    if top == end:
      break

    for neighbour, edge_weight in graph[top].items():
      if neighbour in visited:
        continue

      if dist[neighbour] > topdist + edge_weight:
        dist[neighbour] = topdist + edge_weight
        prev[neighbour] = top
        heappush(pq, (dist[neighbour], neighbour))

    visited.add(top)

  stack = []
  while end != start:
    stack.append(end)
    end = prev[end]
  stack.append(start)
  print(" -> ".join(stack[::-1]))

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print("=== Dijkstra ===")
    print(edges)
    print("A -> E:")
    print(dijkstra(edges, "A", "E"))
    print("F -> G:")
    print(dijkstra(edges, "F", "G"))
