# day10.py
from helper import read_to_integer_matrix

def day_10(input_text):
  print("\n**********************************************************")
  print("************************* Day 10 *************************")
  print("**********************************************************")

  matrix = read_to_integer_matrix(input_text)
  trailhead_sum = calculate_trailhead_scores(matrix)
  print(f"Trailhead score sum is: {trailhead_sum}")


def inbounds(matrix, i, j):
  return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])


def bfs(matrix, i, j):
  queue = [(i, j)]
  trailhead_count = 0
  visited = set()
  directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

  while queue:
    i, j = queue.pop(0)
    visited.add((i, j))
    height = matrix[i][j]

    for x, y in directions:
      new_i = i + x
      new_j = j + y

      if inbounds(matrix, new_i, new_j) and (new_i, new_j) not in visited:
        if matrix[new_i][new_j] == height + 1:
          if matrix[new_i][new_j] == 9:
            trailhead_count += 1
            visited.add((new_i, new_j))
          else:
            queue.append((new_i, new_j))

  return trailhead_count


def calculate_trailhead_scores(matrix):
  # First loop should go through every position in the matrix to find a 0
  # When a 0 is found, begin a breadth first search that will add to the queue everytime the new position is an increment of 1 from the current position
    # Don't forget to store previous positions in a set to prevent dulicates
  # If a nine is reached, add it to the trailheads count
  
  total_count = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        total_count += bfs(matrix, i, j)

  return total_count