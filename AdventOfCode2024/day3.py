# day3.py
import re

def day_3(input_text):
  print("\n**********************************************************")
  print("************************* Day 3 **************************")
  print("**********************************************************")

  multiplications = read_corrupted_file(input_text)
  print(f"Total number of multiplications add up to {multiplications}")

  new_multiplications = read_corrupted_file_with_do_and_dont(input_text)
  print(f"Total number of multiplications after extra instructoins add up to {new_multiplications}\n")


def calculate_multiplications(multiple):
  final_addition = 0
  for mul in multiple:
    s = list(map(int, mul[4:-1].split(',')))
    final_addition += (s[0] * s[1])
  
  return final_addition


def read_corrupted_file(input_file_name):
  multiple = []

  # Open input file for reading
  try:
    with open(input_file_name, "r") as file:

      # Iterate through each line of the input file
      while line := file.readline():
        multiple += re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)", line)
      
  except IOError:
    print("Error: Could not read file " + input_file_name)
  
  return calculate_multiplications(multiple)


def calculate_multiplications_with_instructions(multiple):
  final_addition = 0
  skip = False
  for mul in multiple:
    if mul == "don't()":
      skip = True
      continue
    elif mul == "do()":
      skip = False
      continue

    if not skip:
      s = list(map(int, mul[4:-1].split(',')))
      final_addition += (s[0] * s[1])
  
  return final_addition


def read_corrupted_file_with_do_and_dont(input_file_name):
  multiple = []

  # Open input file for reading
  try:
    with open(input_file_name, "r") as file:

      # Iterate through each line of the input file
      while line := file.readline():
        multiple += re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don't\(\)", line)
      
  except IOError:
    print("Error: Could not read file " + input_file_name)
  

  return calculate_multiplications_with_instructions(multiple)