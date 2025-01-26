# day12.py
from helper import read_to_char_matrix

def day_12(input_text):
  print("\n**********************************************************")
  print("************************* Day 12 *************************")
  print("**********************************************************")

  garden_plot = read_to_char_matrix(input_text)
  fence_cost = calculate_fence_cost(garden_plot)
  print(f"The total cost of fence is: {fence_cost}")


def calculate_fence_cost(garden_plot):
  return len(garden_plot)