# day15.py

def day_15(input_text):
  print("\n**********************************************************")
  print("************************* Day 15 *************************")
  print("**********************************************************")

  gps = read_custom_input(input_text)
  sum_of_gps_coordinates = calculate_player_movement(gps)
  print(f"The sum of all boxes' GPS coordinates is: {sum_of_gps_coordinates}")


class GPS_Details():
  def __init__(self):
    self.width = 0
    self.height = 0
    self.box = set()
    self.obstacle = set()
    self.player = list()
    self.sequence = list()

  def update_player(self, i, j):
    self.player = [i, j]

  def add_to_box(self, i, j):
    self.box.add((i, j))
  
  def remove_from_box(self, i, j):
    self.box.remove((i, j))

  def calculate_sum_of_coordinates(self):
    sum_of_coordinates = 0

    for box in self.box:
      sum_of_coordinates += (100 * (box[0] + 1)) + box[1] + 1
    
    return sum_of_coordinates
  
  def print(self):
    print("Width: ", self.width, "  Height: ", self.height, "\n")
    print(("#" * (self.width + 2)))
    for i in range(self.height):

      line = "#"
      for j in range(self.width):
        if (i, j) in self.box:
          line += "O"
        elif (i, j) in self.obstacle:
          line += "#"
        elif [i, j] == self.player:
          line += "@"
        else:
          line += "."
      
      line += "#"
      print(line)
    
    print(("#" * (self.width + 2)), "\n")
    # print("Sequence: ", self.sequence, "\n")


 
def read_custom_input(input_text):
  gps = GPS_Details()
  """
  Stage 1 reads the width of the matrix
  Stage 2 reads each line and stores the position of objects, obstacles, and the player position
  Stage 3 reads the sequence
  """
  stage = 1
  height = 0
  try:
    with open(input_text, "r") as file:

      while line := file.readline():
        if stage == 1:
          gps.width = len(line) - 3
          stage = 2

        elif stage == 2:
          if line == "\n":
            stage = 3
            gps.height = height - 1
            continue
            
          for i, c in enumerate(line[1:-2]):
            if c == "O":
              gps.box.add((height, i))
            elif c == "#":
              gps.obstacle.add((height, i))
            elif c == "@":
              gps.player = [height, i]
            
          height += 1

        elif stage ==  3:
          if line[-1] == "\n":
            line = line[:-1]
          
          gps.sequence += list(line)
  except IOError:
    print("Error: Could not read file " + input_text)
  
  return gps


def in_range(w, h, i, j):
  return 0 <= i < h and 0 <= j < w


def is_box_not_an_obstable(gps, i, j, direction):
  
  while (i, j) in gps.box:
    i += direction[0]
    j += direction[1]
  
  if (i, j) in gps.obstacle or not in_range(gps.width, gps.height, i, j):
    return False
  else:
    gps.add_to_box(i, j)
    return True


def calculate_player_movement(gps):
  directions = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
  }

  for next in gps.sequence:
    pos = gps.player

    new_i = pos[0] + directions[next][0]
    new_j = pos[1] + directions[next][1]

    # Check if we can move
    if (new_i, new_j) not in gps.obstacle and in_range(gps.width, gps.height, new_i, new_j):

      # easy case, we no boxes in the way
      if (new_i, new_j) not in gps.box:
        gps.update_player(new_i, new_j)
        # two cases, we can move the boxes or we cannot
      elif is_box_not_an_obstable(gps, new_i, new_j, directions[next]):
        gps.update_player(new_i, new_j)
        gps.remove_from_box(new_i, new_j)     

  # Do something with the box positions
  return gps.calculate_sum_of_coordinates()