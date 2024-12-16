from helper import read_to_list, read_to_integer_matrix, read_to_char_matrix
from day1 import day_1
from day2 import day_2
from day3 import day_3
from day4 import day_4
from day5 import day_5
from day6 import day_6
from day7 import day_7

import sys


def main():
  days = [day_1, day_2, day_3, day_4, day_5, day_6, day_7]

  try:
    query = sys.argv[1]
  except ValueError:
    print("Please provide a valid integer or range")
    sys.exit(1) 

  if query.isnumeric():
    query = int(query)

    if query < 1 or query > 25:
      print("\nInputed day was not between 1 and 25. Printing day 1 results instead")
      days[0]()
    else:
      days[query - 1]()
  else:
    start, end = query.split("-")
    start = int(start)
    end = int(end)

    if start < 1 or end > 25:
      print("\nInputed day range was not between 1 and 25. Printing day 1 results instead")
      days[0]()
    else:
      for i in range(start-1, end):
        days[i]()


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <number> or python3 main.py <start-end>")
    sys.exit(1)
  
  main()


