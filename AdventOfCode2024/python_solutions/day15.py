# day15.py

def day_15(input_text):
  print("\n**********************************************************")
  print("************************* Day 15 *************************")
  print("**********************************************************")

  sum_of_gps_coordinates = read_custom_input(input_text)
  print(f"The sum of all boxes' GPS coordinates is: {sum_of_gps_coordinates}")


def read_custom_input(input_text):
  return 0