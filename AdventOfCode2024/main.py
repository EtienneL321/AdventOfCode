from python_solutions.day1 import day_1
from python_solutions.day2 import day_2
from python_solutions.day3 import day_3
from python_solutions.day4 import day_4
from python_solutions.day5 import day_5
from python_solutions.day6 import day_6
from python_solutions.day7 import day_7
from python_solutions.day8 import day_8
from python_solutions.day9 import day_9

import sys

def file_name(num, test):
  if test:
    return f"./AdventOfCode2024/puzzle_inputs/day_{num}_test_input.txt"
  else:
    return f"./AdventOfCode2024/puzzle_inputs/day_{num}_input.txt"

def main():
  days = [day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8, day_9]

  try:
    query = sys.argv[1]

    test = False
    if len(sys.argv) == 3 and sys.argv[2] == "-t":
      test = True
  except ValueError:
    print("Please provide a valid integer or range")
    sys.exit(1) 

  if query.isnumeric():
    query = int(query)

    if query < 1 or query > 25:
      print("\nInputed day was not between 1 and 25. Printing day 1 results instead")
      days[0](file_name(1, test))
    else:
      days[query - 1](file_name(query, test))
  else:
    start, end = query.split("-")
    start = int(start)
    end = int(end)

    if start < 1 or end > 25 or end < start:
      print("\nInputed day range was not between 1 and 25 or has an incorrect order. Printing day 1 results instead")
      days[0](file_name(1, test))
    else:
      for i in range(start-1, end):
        days[i](file_name(i+1, test))


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <number> or python3 main.py <start-end>")
    sys.exit(1)
  
  main()


