# day6.py
from helper import read_to_char_matrix

def day_6():
  print("\n**********************************************************")
  print("************************* Day 6 **************************")
  print("**********************************************************")

  maze_matrix = read_to_char_matrix("./inputs/day_6_input.txt")

  distinct_positions = find_guard_path(maze_matrix)
  print(f"The guard moves to {distinct_positions} distinct positions")

  obstacle_moves = infinite_loop_glitch(maze_matrix)
  print(f"The number of places an obstacle can be added to create a loop is {obstacle_moves}")


def find_start_of_maze(matrix):
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      if matrix[row][col] == "^":
        return [row, col]


def in_bounds(matrix, position):
  row_l = len(matrix)
  col_l = len(matrix[0])

  row = position[0]
  col = position[1]

  return 0 <= row < row_l and 0 <= col < col_l


def update_position(position, d_index, increment=True):
  directions = [[-1,0],[0,1],[1,0],[0,-1]] 

  if increment:
    position[0] += directions[d_index][0]
    position[1] += directions[d_index][1]
  else:
    position[0] -= directions[d_index][0]
    position[1] -= directions[d_index][1]


def change_direction(position, d_index):
  update_position(position, d_index, False)

  # change direction index
  if d_index == 3:
    d_index = 0
  else:
    d_index += 1

  return d_index


def find_guard_path(matrix):
  position = find_start_of_maze(matrix) # tuple of starting position
  visited = set() # set to store all unique positions
  d_index = 0 # starting direction is going up

  while in_bounds(matrix, position):
    row = position[0]
    col = position[1]
    
    # check for obstacle
    if matrix[row][col] == "#":
      d_index = change_direction(position, d_index)
    
    # check for unique position
    elif tuple(position) not in visited:
      visited.add(tuple(position))

    # Move
    update_position(position, d_index)

  return len(visited)


def is_new_path_a_loop(matrix, position):
  # How is a loop identified?
  # First approach - store the start location and return if the current position equals the start again
  # Result - infinite loop when start is not part of the loop
  #
  # Second approach - store all previous locations and return if the current position overlaps with previous positions
  # Result - crossing the path causes a false positive
  #
  # Third approach - store all previous obstacles and return when the same obstacle is visited more than once
  # Result - false positive when an obstacle is used from different directions
  #
  # Fourth approach - store all previous obstacles with the approached direction and return when both approach and obstacle are repeated
  # Result - did not account for duplicate obstacle positions causing more than one loop
  #
  # Fifth approach - consider intersections (only check for obstacle validity the first time) and iterate through the path in the correct order
  # Result - intersections were only checked if it caused a valid new obstacle
  #
  # Sixth approach - store all previous obstacles to prevent addition of duplicates
  # Result - down to 1739 but still a failure
  #
  # Seventh approach - start each iteration from the start (even though we should be able to start from right before the obstacle)
  # Result - success with 1697
  #
  # Lessons learned
  # Testing is difficult when it is not easy to write test cases. Moreover, I think I started off too complicated. From here, I
  # could try to start from right before the obstacle but it there were MULTIPLE bugs in my code which made this implementation
  # very difficult from the start. In the future, it's better for me to start with the easier solution and improve from there.

  d_index = 0
  visited_obstacle = set() # we log visits at obstacles and their direction

  while in_bounds(matrix, position):
    #print(position)
    row = position[0]
    col = position[1]

    # check for obstacle
    if matrix[row][col] == "#":

      # check if obstacle was already visited
      if tuple(position + [d_index]) in visited_obstacle:
        return True
      
      # we have not visited this obstacle
      else:
        visited_obstacle.add(tuple(position + [d_index]))
        d_index = change_direction(position, d_index)
      
    # Move
    update_position(position, d_index)

  return False


def infinite_loop_glitch(matrix):
  # step 1: get the path of the guard
  # step 2: iterate through the path in reverse
  # step 3: at every position, add an obstacle and rotate the guard 90 degrees
  # step 4: evaluate the path of the guard to see if it creates a loop

  position = find_start_of_maze(matrix)
  start = tuple(position)

  new_obstacle_positions = 0
  visited = set()
  visited.add(start)

  d_index = 0

  # Move one position from the start
  update_position(position, d_index)

  # step 1
  while in_bounds(matrix, position):
    row = position[0]
    col = position[1]
    
    # check for obstacle
    if matrix[row][col] == "#":
      d_index = change_direction(position, d_index)
    
    # step 2
    elif tuple(position) not in visited:
      # add new obstacle
      matrix[row][col] = "#"

      if is_new_path_a_loop(matrix, list(start)):
        new_obstacle_positions += 1
      
      # revert to regular path
      matrix[row][col] = "."
      
      visited.add(tuple(position))

    # Move
    update_position(position, d_index)

  return new_obstacle_positions