# day15.py

def day_15(input_text):
  print("\n**********************************************************")
  print("************************* Day 15 *************************")
  print("**********************************************************")

  gps = read_custom_input(input_text)
  # gps.print()
  sum_of_gps_coordinates = calculate_player_movement(gps)
  print(f"The sum of all boxes' GPS coordinates is: {sum_of_gps_coordinates}")

class Box():
  def __init__(self, h, left, right):
    self.height = h
    self.left = left
    self.right = right
  
  def __eq__(self, box):
    if isinstance(box, Box):
      return self.height == box.height and self.left == box.left and self.right == box.right
    return False
  
  def __hash__(self):
    return hash((self.height, self.left, self.right))
  
  def in_range(self, h, w):
    return 0 <= self.height < h and 0 <= self.left and self.right < w


class GPS_Details():
  def __init__(self):
    self.width = 0
    self.height = 0
    self.box = set()
    self.obstacle = set()
    self.wide_obstacle = set()
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

  def calculate_sum_of_wide_coordinates(self):
    sum_of_coordinates = 0

    for box in self.box:
      sum_of_coordinates += (100 * (box.height + 1)) + box.left + 2
    
    return sum_of_coordinates
  
  def print(self):
    print("Width: ", self.width, "  Height: ", self.height, "\n")
    print(("#" * (self.width + 4)))
    for i in range(self.height):

      line = "##"
      j = 0
      while j < self.width:
        box = Box(i, j, j + 1)
        if box in self.box:
          line += "[]"
          j += 1
        elif (i, j) in self.obstacle:
          line += "#"
        elif [i, j] == self.player:
          line += "@"
        else:
          line += "."
        
        j += 1
      
      line += "##"
      print(line)
    
    print(("#" * (self.width + 4)), "\n")
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
          gps.width = (len(line) - 3) * 2
          stage = 2

        elif stage == 2:
          if line == "\n":
            stage = 3
            gps.height = height - 1
            continue
            
          for i, c in enumerate(line[1:-2]):
            if c == "O":
              gps.box.add(Box(height, (i*2), (i*2) + 1))
            elif c == "#":
              gps.wide_obstacle.add(Box(height, (i*2), (i*2) + 1))
              gps.obstacle.add((height, (i*2)))
              gps.obstacle.add((height, (i*2) + 1))
            elif c == "@":
              gps.player = [height, i*2]
            
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
  

def box_is_not_an_obstacle_horizontal(gps, box, direction):
  if box in gps.wide_obstacle:
    return False
  elif box not in gps.box:
    return True

  m_box = Box(box.height, box.left + direction[1], box.right + direction[1])

  if m_box.in_range(gps.height, gps.width):
    if box_is_not_an_obstacle_horizontal(gps, Box(m_box.height, m_box.left + direction[1], m_box.right + direction[1]), direction):
      gps.box.add(m_box)
      gps.box.remove(box)
      return True
    else:
      return False
  else:
    return False


def box_is_not_an_obstacle_vertical(gps, box, direction):
  l_box = Box(box.height + direction[0], box.left - 1, box.right - 1)
  m_box = Box(box.height + direction[0], box.left, box.right)
  r_box = Box(box.height + direction[0], box.left + 1, box.right + 1)

  if l_box in gps.wide_obstacle or m_box in gps.wide_obstacle or r_box in gps.wide_obstacle or not m_box.in_range(gps.height, gps.width):
    return False

  state = True
  if l_box in gps.box or m_box in gps.box or r_box in gps.box:
    if l_box in gps.box:
      state &= box_is_not_an_obstacle_vertical(gps, l_box, direction)
    
    if m_box in gps.box:
      state &= box_is_not_an_obstacle_vertical(gps, m_box, direction)
    
    if r_box in gps.box:
      state &= box_is_not_an_obstacle_vertical(gps, r_box, direction)
  else:
    return True
  
  if state:
    if l_box in gps.box:
      gps.box.add(Box(l_box.height + direction[0], l_box.left, l_box.right))
      gps.box.remove(l_box)
    
    if m_box in gps.box:
      gps.box.add(Box(m_box.height + direction[0], m_box.left, m_box.right))
      gps.box.remove(m_box)
    
    if r_box in gps.box:
      gps.box.add(Box(r_box.height + direction[0], r_box.left, r_box.right))
      gps.box.remove(r_box)
    
    return True
  else:
    return False

  

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
      
      l_box = Box(new_i, new_j-1, new_j)
      r_box = Box(new_i, new_j, new_j+1)
      if l_box in gps.box:
        if directions[next][0] == 0:
          if box_is_not_an_obstacle_horizontal(gps, l_box, directions[next]):
            gps.update_player(new_i, new_j)
        else:
          if box_is_not_an_obstacle_vertical(gps, l_box, directions[next]):
            gps.box.add(Box(l_box.height + directions[next][0], l_box.left, l_box.right))
            gps.box.remove(l_box)
            gps.update_player(new_i, new_j)

      elif r_box in gps.box:
        if directions[next][0] == 0:
          if box_is_not_an_obstacle_horizontal(gps, r_box, directions[next]):
            gps.update_player(new_i, new_j)
        else:
          if box_is_not_an_obstacle_vertical(gps, r_box, directions[next]):
            gps.box.add(Box(r_box.height + directions[next][0], r_box.left, r_box.right))
            gps.box.remove(r_box)
            gps.update_player(new_i, new_j)
      else:
        gps.update_player(new_i, new_j)
    
    # print("Next: ", next)
    # gps.print()

  # Do something with the box positions
  return gps.calculate_sum_of_wide_coordinates()