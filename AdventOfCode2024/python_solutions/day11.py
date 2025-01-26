# day11.py
from helper import read_by_line

iterations = 75

def day_11(input_text):
  print("\n**********************************************************")
  print("************************* Day 11 *************************")
  print("**********************************************************")

  # I need to use some dynamic programming to solve for more than 40 iterations
  """
  What i have pictures in my head looks like so
  0 -> 1 (1st) -> 2024 (2nd) -> 20 24 (3rd) -> 2 0 2 4 (4th) -> 4048 1 4048 8096 (5th) ...

  With each iteration, a dictionary is filled up with information on how many nodes are present at each iteration
  (1st iteration)
  0: [1]

  (2nd iteration)
  0: [1, 1]
  1: [1]

  (3rd iteration) 
  
  0: [1, 1, 2]
  1: [1, 2]
  2024: [2]

  (4th iteration)
  0: [1, 1, 2, 4]
  1: [1, 2, 4]
  2024: [2, 4]
  20: [2]
  24: [2]

  (5th iteration)
  0: [1, 1, 2, 4, 4]
  1: [1, 2, 4, 4]
  2024: [2, 4, 4]
  20: [2, 4]
  24: [2, 4]
  2: [1]
  4: [1]

  Once we get to this stage, 0 is reused. We check to see if the numbers of iterations for 0 (currently size 5) is
  greater than or equal to iterations - current iteration (5). If it is, then we can return the number of nodes at
  that iteration. If not, we add to the iteration node count. (still not 100% sure how this part will be done yet)
  """
  number_of_stones = read_by_line(input_text, stone_count)
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

  for _ in range(iterations):
    int_line, str_line = blink(int_line, str_line)
    # print(int_line)
    # print(str_line)

  return len(int_line)


def stone_count(input):
  num_inputs = list(map(int, input.split(" ")))

  total_stone_count = 0
  for num in num_inputs:
    # print(f"########### Calculating stones for {num} ############")
    mem = dp_blink(num, iterations)
    # print(mem, num)
    total_stone_count += mem[0]
  
  return total_stone_count

stone_dict = dict()

def dp_blink(num, iter):
  if iter == 0:
    return []
  
  if num in stone_dict and len(stone_dict[num]) >= iter:
    # print("Exception", stone_dict[num], "for iteration", iterations - iter, "and num", num, ". The remaining iterations are", iter, "So i need to return", stone_dict[num][len(stone_dict[num]) - iter:])
    return stone_dict[num][len(stone_dict[num]) - iter:]

  str_num = str(num)
  increment_type = 1 # 1 for incrementing by 1, 2 for incrementing by 2
  if num == 0:
    mem = dp_blink(1, iter - 1)
  elif len(str_num) % 2 == 0:
    increment_type = 2

    half = len(str_num) // 2
    left = str_num[:half]
    right = str_num[half:]

    right = right.lstrip('0')

    if right == '':
      right = '0'
    
    left_mem = dp_blink(int(left), iter - 1)
    right_mem = dp_blink(int(right), iter - 1)
    
    mem = add_lists(left_mem, right_mem)
  else:
    mem = dp_blink(num * 2024, iter - 1)

  stone_dict[num] = mem + [increment_type]
  
  return stone_dict[num]


def add_lists(list1, list2):
  new_list = []
  l = min(len(list1), len(list2))

  for i in range(l):
    new_list.append(list1[i] + list2[i])
  
  if len(list1) > len(list2):
    new_list += list1[l:]
  else:
    new_list += list2[l:]
  
  return new_list