# day11.py
from helper import read_by_line
import datetime

iterations = 75

def day_11(input_text):
  print("\n**********************************************************")
  print("************************* Day 11 *************************")
  print("**********************************************************")

  number_of_stones = read_by_line(input_text, get_stone_count)
  print(f"The number of stones after {iterations} iterations is: {number_of_stones}")


d = {
  '0': 0,
  '1': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9
}

d_reverse = {
  0: '0',
  1: '1',
  2: '2',
  3: '3',
  4: '4',
  5: '5',
  6: '6',
  7: '7',
  8: '8',
  9: '9'
}

def str_to_int(input):
  output = 0

  factor = 1
  for i in range(1, len(input) + 1):
    output += d[input[-i]] * factor

    factor *= 10
  
  return output


def int_to_str(input):
  output = ""

  while input > 0:
    output = d_reverse[input % 10] + output
    input //= 10

  return output


def blink(int_line, str_line):
  new_int_line = []
  new_str_line = []
  i = 0
  while i < len(int_line):
    if not int_line[i]:
      new_int_line.append(1)
      new_str_line.append('1')

    elif len(str_line[i]) % 2 == 0:
      left = str_line[i][:(len(str_line[i]) // 2)]
      right = str_line[i][(len(str_line[i]) // 2):]

      right = right.lstrip('0')

      if right == '':
        right = '0'

      new_int_line.append(str_to_int(left))
      new_int_line.append(str_to_int(right))
      new_str_line.append(left)
      new_str_line.append(right)

    else:
      new_int_line.append(int_line[i] * 2024)
      new_str_line.append(int_to_str(int_line[i] * 2024))
    
    i += 1

  return (new_int_line, new_str_line)
    

def get_stone_count(input):
  int_line = list(map(int, input.split(" ")))
  str_line = input.split(" ")
  print(int_line)

  for i in range(iterations):
    print(f"iteration: {i}  time: {datetime.datetime.now()}")
    int_line, str_line = blink(int_line, str_line)
    # print(int_line)
    # print(str_line)

  return len(int_line)