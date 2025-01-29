# day13.py
import re

def day_13(input_text):
  print("\n**********************************************************")
  print("************************* Day 13 *************************")
  print("**********************************************************")

  read_button_input(input_text)
  tokens_spend = calculate_button_presses()
  print(f"The total number of tokens spent is : {tokens_spend}")


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class ClawGame:
  def __init__(self, A, B, prize):
    self.A = Point(A[0], A[1])
    self.B = Point(B[0], B[1])
    self.prize = Point(prize[0], prize[1])

  def print_game(self):
    print(f"A: {self.A.x}, {self.A.y}")
    print(f"B: {self.B.x}, {self.B.y}")
    print(f"Prize: {self.prize.x}, {self.prize.y}")

games = list()

b_press_price = 1
a_press_price = 3

"""
Stores button A and B increments as well as the prize location
"""
def read_button_input(input_file_name):
  # Open input file for reading
  try:
    with open(input_file_name, "r") as file:

      # Iterate through each line of the input file
      step = 0
      A = []
      B = []
      prize = []
      while line := file.readline():
        if line == "\n":
          continue

        if step == 0:
          A = list(map(int, re.findall(r"\d+", line)))
          step += 1
        elif step == 1:
          B = list(map(int, re.findall(r"\d+", line)))
          step += 1
        elif step == 2:
          prize = list(map(int, re.findall(r"\d+", line)))
          games.append(ClawGame(A, B, prize))
          step = 0
      
  except IOError:
    print("Error: Could not read file " + input_file_name)


def calculate_button_presses():
  total_button_price = 0
  for game in games:
    # game.print_game()
    total_button_price += play_game(game)

  return total_button_price


def play_game(game):
  num = game.prize.y * game.B.x - game.prize.x * game.B.y
  dem = game.A.y * game.B.x - game.B.y * game.A.x
  A = num // dem

  temp = game.prize.x - game.A.x * A
  B = temp // game.B.x
  
  # Check
  button_price = 0
  if A * game.A.y + B * game.B.y == game.prize.y and A * game.A.x + B * game.B.x == game.prize.x:
    # print("Success")
    button_price = A * a_press_price + B * b_press_price

  return button_price
    
