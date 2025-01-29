# day12.py
from helper import read_to_char_matrix
from collections import deque

def day_12(input_text):
  print("\n**********************************************************")
  print("************************* Day 12 *************************")
  print("**********************************************************")

  garden_plot = read_to_char_matrix(input_text)
  fence_cost = calculate_fence_cost(garden_plot)
  print(f"The total cost of fence is: {fence_cost}")

visited = set() # stores every visited node in the garden plot

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def in_range(garden_plot, i, j):
  return i >= 0 and i < len(garden_plot) and j >= 0 and j < len(garden_plot[i])

def calculate_fence_cost(garden_plot):
  total_price = 0

  for i in range(len(garden_plot)):
    for j in range(len(garden_plot[i])):
      if (i, j) not in visited:
        # print("Starting at: ", i, j)
        total_price += get_region_price(garden_plot, i, j)
      
  return total_price


def get_region_price(garden_plot, x, y):
  # store current region in area
  region = garden_plot[x][y]

  region_visited = set() # stores every visited node in the region
  queue = deque(list())
  queue.append((x, y))
  visited.add((x, y)) # populate visited
  region_visited.add((x, y)) # populate region visited

  perim = 4
  area = 0
  while len(queue) != 0:
    i, j = queue.popleft()
    area += 1

    for d in directions:
      new_i = i + d[0]
      new_j = j + d[1]

      if valid_plant(garden_plot, new_i, new_j, region):
        queue.append((new_i, new_j))
        visited.add((new_i, new_j)) # populate visited
        region_visited.add((new_i, new_j)) # populate region visited
        perim += get_perimeter(region_visited, new_i, new_j)
  
  # print("Region: ", region, " Area: ", area, " Perimeter: ", perim)
  return perim * area


"""
Return the perimeter this new fence would add
If plant is not valid, return -1

Check that we are
1. in range
2. have the same region type
3. have not been visited yet
"""
def valid_plant(garden_plot, i, j, region):
  return in_range(garden_plot, i, j) and garden_plot[i][j] == region and (i, j) not in visited


"""
Return the perimeter this new fence would add
every new neighbor adds 2 to the perimeter unless it touches 2 other neighbors
"""
def get_perimeter(region_visited, i, j):
  perim = 2
  counter = 2
  for d in directions:
    new_i = i + d[0]
    new_j = j + d[1]

    if (new_i, new_j) in region_visited:
      counter -= 1
        
  if counter <= 0: # if counter is equal to or below 0, we have more than one neighbor
    perim = 0
  
  return perim
