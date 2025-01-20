# day10.py
from helper import read_to_char_matrix

def day_10(input_text):
  print("\n**********************************************************")
  print("************************* Day 10 *************************")
  print("**********************************************************")

  matrix = read_to_char_matrix(input_text)
  trailhead_sum = calculate_trailhead_scores(matrix)
  print(f"Trailhead score sum is: {trailhead_sum}")


def calculate_trailhead_scores(matrix):
  # First loop should go through every position in the matrix to find a 0
  # When a 0 is found, begin a breadth first search that will add to the queue everytime the new position is an increment of 1 from the current position
    # Don't forget to store previous positions in a set to prevent dulicates
  # If a nine is reached, add it to the trailheads count

  return 1