# day16.py
from helper import read_to_char_matrix
import heapq
from collections import deque

def day_16(input_text):
  print("\n**********************************************************")
  print("************************* Day 16 *************************")
  print("**********************************************************")

  matrix = read_to_char_matrix(input_text)
  lowest_score = calculate_lowest_movement_score(matrix)

  print(f"The lowest score a reindeer could get is: {lowest_score}")


transition_distance = {
  ('>', 'v'): 1001, # Corner
  ('v', '<'): 1001, # Corner
  ('<', '^'): 1001, # Corner
  ('>', '^'): 1001, # Corner
  ('v', '^'): 1,    # Straight line
  ('>', '<'): 1,    # Straight line
  ('<', '>'): 1,    # Straight line
  ('^', 'v'): 1,    # Straight line
  ('>',): 1,         # Dead end
  ('v',): 1,         # Dead end
  ('<',): 1,         # Dead end
  ('^',): 1,         # Dead end
}

directions = {
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1),
  '^': (-1, 0)
}

adj = {}

class Point():
  def __init__(self, i, j, iter = 0):
    self.i = i
    self.j = j
    self.iter = iter # Iteration 0 is the original point. This value only changes for special nodes (intersections)
    self.edges = []
  
  def __eq__(self, other):
    return self.i == other.i and self.j == other.j and self.iter == other.iter
  
  def __str__(self):
    return f"({self.i}, {self.j}){self.iter}"
  
  def __repr__(self):
    return f"({self.i}, {self.j}){self.iter}"

  def __hash__(self):
    return hash((self.i, self.j))

  def move(self, direction):
    return Point(self.i + direction[0], self.j + direction[1])
  
  def value(self, matrix):
    return matrix[self.i][self.j]
  
  def not_in(self, visited):
    return self not in visited


class Node():
  def __init__(self, key, distance):
    self.key = key
    self.distance = distance

  def __lt__(self, other):
    return self.distance < other.distance

  def __str__(self):
    return f"({self.key}, {self.distance})"
  
  def __repr__(self):
    return f"({self.key}, {self.distance})"


def calculate_lowest_movement_score(matrix):
  # We are going to implement Dijkstra's algorithm
  # We need to start by creating an adjacency map
  start = Point(len(matrix) - 2, 1)
  end = Point(1, len(matrix[0]) - 2)

  to_visit = set()
  special_node = set()
  create_adjacency_map(matrix, start, to_visit, special_node)
  print(to_visit)
  for p in to_visit:
    if p.value(matrix) == 'S':
      populate_start(p)
    else:
      populate_adjacency_map(p, special_node)
  
  for a in adj:
    print(a, adj[a])
  
  # Dijkstra's algorithm
  path = dijkstra_algorithm(start, end, adj)
  path_backtrack(start, end, path, matrix)

  return len(matrix)


def path_backtrack(start, end, path, matrix):
  current = path[end]
  while current.key != start:
    matrix[current.key.i][current.key.j] = '^'
    current = path[current.key]
  
  # Print the path
  for row in matrix:
    s = " ".join(row)
    print(s)


def dijkstra_algorithm(start, end, adj):
  visited = set()
  path = {}
  q = list()

  path[start] = Node(start, 0)
  heapq.heappush(q, path[start])

  while len(q) != 0:
    n = heapq.heappop(q)
    key = n.key
    distance = n.distance
    visited.add(key)

    adj_list = adj[key]
    for adj_link in adj_list:
      if adj_link[0] not in visited:
        if adj_link[0] not in path:
          path[adj_link[0]] = Node(key, distance + adj_link[1])
        else:
          node_copy = path[adj_link[0]]
          if distance + adj_link[1] < node_copy.distance:
            node_copy.distance = distance + adj_link[1]
            node_copy.key = key
        heapq.heappush(q, Node(adj_link[0], distance + adj_link[1]))
  
  for key in path:
    print(key, path[key])

  print("end", path[end])
  return path


def create_adjacency_map(matrix, start, to_visit, special_node):
  visited = set()
  q = deque()
  q.append(start)

  while len(q) != 0:
    p = q.popleft()
    visited.add(p)

    for dir, adjustment in directions.items():
      new_p = p.move(adjustment)
      if new_p.value(matrix) != '#':
        if new_p.not_in(visited):
          q.append(new_p)
        p.edges.append(dir)
    
    if len(p.edges) >= 3:
      populate_intersection(p, matrix)
      special_node.add(p)
    else:
      to_visit.add(p)


def initialize_points_and_adj(p, num_points):
  points = [Point(p.i, p.j, i + 1) for i in range(num_points)]
  for point in points:
    adj[point] = []
  return points


def ensure_adj_for_neighbors(neighbors):
  for neighbor in neighbors:
    if neighbor not in adj:
      adj[neighbor] = []


def add_bidirectional_edge(a, b, weight_a_to_b, weight_b_to_a):
  adj[a].append((b, weight_a_to_b))
  adj[b].append((a, weight_b_to_a))


def populate_intersection(p, matrix):
  neighbors = {
      'left': p.move(directions['<']),
      'right': p.move(directions['>']),
      'up': p.move(directions['^']),
      'down': p.move(directions['v']),
    }
  
  if len(p.edges) == 4:
    points = initialize_points_and_adj(p, 6)
    ensure_adj_for_neighbors(neighbors.values())

    # Populate adjacency lists for 4 edges
    add_bidirectional_edge(neighbors['right'], points[0], 1, 1001)
    add_bidirectional_edge(points[0], neighbors['down'], 1001, 1)
    add_bidirectional_edge(neighbors['down'], points[1], 1, 1001)
    add_bidirectional_edge(points[1], neighbors['left'], 1001, 1)
    add_bidirectional_edge(neighbors['left'], points[2], 1, 1001)
    add_bidirectional_edge(points[2], neighbors['up'], 1001, 1)
    add_bidirectional_edge(neighbors['up'], points[3], 1, 1001)
    add_bidirectional_edge(points[3], neighbors['right'], 1001, 1)

    # Cross edges
    add_bidirectional_edge(neighbors['left'], points[4], 1, 1)
    add_bidirectional_edge(points[4], neighbors['right'], 1, 1)
    add_bidirectional_edge(neighbors['up'], points[5], 1, 1)
    add_bidirectional_edge(points[5], neighbors['down'], 1, 1)

  elif len(p.edges) == 3:
    # Need to add a case where one or more of the cross edges are corners
    # Need to add a case where a T intersection is next to a T intersection
    points = initialize_points_and_adj(p, 3)
    edges_config = {
      ('>', 'v', '^'): ('up', 'right', 'down'),
      ('>', 'v', '<'): ('right', 'down', 'left'),
      ('v', '<', '^'): ('down', 'left', 'up'),
      ('>', '<', '^'): ('left', 'up', 'right'),
    }
    edges_remove = {
      ('>', 'v', '^'): ('left'),
      ('>', 'v', '<'): ('up'),
      ('v', '<', '^'): ('right'),
      ('>', '<', '^'): ('down'),
    }
    directions_order = edges_config[tuple(p.edges)]
    del neighbors[edges_remove[tuple(p.edges)]]
    ensure_adj_for_neighbors(neighbors.values())

    # Cross edges
    if is_corner(neighbors[directions_order[0]], matrix):
      add_bidirectional_edge(neighbors[directions_order[0]], points[2], 1001, 1)
      add_bidirectional_edge(neighbors[directions_order[0]], points[0], 1001, 1001)
    else:
      add_bidirectional_edge(neighbors[directions_order[0]], points[2], 1, 1)
      add_bidirectional_edge(neighbors[directions_order[0]], points[0], 1, 1001)
    
    if is_corner(neighbors[directions_order[1]], matrix):
      add_bidirectional_edge(points[0], neighbors[directions_order[1]], 1001, 1001)
      add_bidirectional_edge(neighbors[directions_order[1]], points[1], 1001, 1001)
    else:
      add_bidirectional_edge(points[0], neighbors[directions_order[1]], 1001, 1)
      add_bidirectional_edge(neighbors[directions_order[1]], points[1], 1, 1001)

    if is_corner(neighbors[directions_order[2]], matrix):
      add_bidirectional_edge(points[2], neighbors[directions_order[2]], 1001, 1)
      add_bidirectional_edge(points[1], neighbors[directions_order[2]], 1001, 1001)
    else:
      add_bidirectional_edge(points[2], neighbors[directions_order[2]], 1, 1)
      add_bidirectional_edge(points[1], neighbors[directions_order[2]], 1001, 1)


def is_corner(p, matrix):
  edges = []
  for dir, adjustment in directions.items():
    new_p = p.move(adjustment)
    if new_p.value(matrix) != '#':
      edges.append(dir)

  print(tuple(edges))
  if len(edges) < 3 and transition_distance[tuple(edges)] == 1001:
    return True
  else:
    return False



def populate_start(p):
  if p not in adj:
        adj[p] = []

  for edge in p.edges:
    new_p = p.move(directions[edge])
    if edge == '>':
      adj[p].append((new_p, 1))
    elif edge == 'v':
      adj[p].append((new_p, 1001))
    elif edge == '^':
      adj[p].append((new_p, 1001))
    else:
      adj[p].append((new_p, 2001))


def populate_adjacency_map(p, special_node):
  if p not in adj:
        adj[p] = []

  distance = transition_distance[tuple(p.edges)]
  for edge in p.edges:
    new_p = p.move(directions[edge])
    if p.i == 4 and p.j == 9:
      print(edge)
    if new_p in special_node:
      continue

    adj[p].append((new_p, distance))