# day14.py
from helper import read_by_line
from collections import defaultdict
import re
import time

def day_14(input_text):
  print("\n**********************************************************")
  print("************************* Day 14 *************************")
  print("**********************************************************")

  safety_score = read_by_line(input_text, get_position_given_time)

  safety_score = 1
  for quadrant in score:
    print(f"Quadrant {quadrant} has {score[quadrant]} stars")
    safety_score *= score[quadrant]
  print(f"Safety score after {elapsed_time} seconds is : {safety_score}")
  
  find_easter_egg(input_text)


class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

elapsed_time = 100

# For test, use width = 11, height = 7
# For actual input, use width = 101, height = 103
width = 101
height = 103

# Store score from quadrants
score = defaultdict(int)

# Store points
disp_points = defaultdict(int)

def get_position_given_time(line):
  temp = list(map(int, re.findall(r"-?\d+", line)))

  position = Point(temp[0], temp[1])
  velocity = Point(temp[2], temp[3])

  position.x += elapsed_time * velocity.x
  position.y += elapsed_time * velocity.y

  # Use modulos operator to handle overflow of values
  if position.x > 0:
    position.x %= width
  else:
    position.x = width - (abs(position.x) % width)

    if position.x == width:
      position.x = 0

  if position.y > 0:
    position.y %= height
  else:
    position.y = height - (abs(position.y) % height)

    if position.y == height:
      position.y = 0
      

  # print(f"New position: {position.x}, {position.y}")

  # Check which quadrant we are in
  if position.x > width // 2 and position.y < height // 2:
    score[1] += 1
  elif position.x < width // 2 and position.y < height // 2:
    score[2] += 1
  elif position.x < width // 2 and position.y > height // 2:
    score[3] += 1
  elif position.x > width // 2 and position.y > height // 2:
    score[4] += 1

  disp_points[(position.x, position.y)] += 1

  return 0


def get_positions(line, elapsed_time):
  temp = list(map(int, re.findall(r"-?\d+", line)))

  position = Point(temp[0], temp[1])
  velocity = Point(temp[2], temp[3])

  position.x += elapsed_time * velocity.x
  position.y += elapsed_time * velocity.y

  # Use modulos operator to handle overflow of values
  if position.x > 0:
    position.x %= width
  else:
    position.x = width - (abs(position.x) % width)

    if position.x == width:
      position.x = 0

  if position.y > 0:
    position.y %= height
  else:
    position.y = height - (abs(position.y) % height)

    if position.y == height:
      position.y = 0

  # Add to dictionary
  disp_points[(position.x, position.y)] += 1

  return 0


def print_graph():
  for i in range(height):
    for j in range(width):
      if (j, i) in disp_points:
        print(disp_points[(j, i)], end="")
      else:
        print(".", end="")
    print("")


def find_easter_egg(input_text):
  lower_bound = 503
  upper_bound = 100000

  easter_egg = 8179
  for i in range(easter_egg, easter_egg + 1, 101):
    disp_points.clear()

    try:
      with open(input_text, "r") as file:

        # Iterate through each line of the input file
        while line := file.readline():
          get_positions(line, i)
      
    except IOError:
      print("Error: Could not read file " + input_text)
    
    print(f"\n\nIteration: {i}",)
    print_graph()
    time.sleep(0.2)
    
  