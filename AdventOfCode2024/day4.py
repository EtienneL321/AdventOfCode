# day4.py
from helper import read_to_char_matrix

def day_4(input_text):
  print("\n**********************************************************")
  print("************************* Day 4 **************************")
  print("**********************************************************")

  char_matrix = read_to_char_matrix(input_text)

  xmas_occurrences = xmas_puzzle_solver(char_matrix)
  print(f"There are a total of {xmas_occurrences} XMAS occurrences.")

  xmas_occurrences = xmas_extreme_puzzle_solver(char_matrix)
  print(f"There are a total of {xmas_occurrences} X-MAS occurrences.\n")



def find_xmas(puzzle, r, c):
  ans = ['M','A','S']
  directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
  num_of_occurrences = 0

  for i, j in directions:
    new_r = r
    new_c = c
    for letter in ans:
      # check that the resulting position is in bounds
      if (0 <= new_r+i < len(puzzle)) and (0 <= new_c+j < len(puzzle[0])):
        new_r += i
        new_c += j
      else:
        break

      # check if letter matches
      if puzzle[new_r][new_c] != letter:
        break
      elif letter == 'S':
        num_of_occurrences += 1
    
  return num_of_occurrences


def xmas_puzzle_solver(puzzle):
  num_of_occurrences = 0

  # For every letter in the puzzle, check all directions for possible XMAS combinations
  for r in range(len(puzzle)):
    for c in range(len(puzzle[0])):
      if puzzle[r][c] != 'X':
        continue
      
      num_of_occurrences += find_xmas(puzzle, r, c)

  return num_of_occurrences


def find_extreme_xmas(puzzle, r, c):
  ans = ['M','M','S','S']
  directions = [[-1,1],[1,1],[1,-1],[-1,-1]]
  num_of_occurrences = 0

  # We have four chances to get a MMSS combinations while rotating clockwise around A
  for _ in range(4):
    # Rotate clockwise
    for k, d in enumerate(directions):
      i = d[0]
      j = d[1]

      # check that the resulting position is in bounds
      if (0 <= r+i < len(puzzle)) and (0 <= c+j < len(puzzle[0])):
        new_r = r + i
        new_c = c + j
      else:
        break

      # check if letter matches
      if puzzle[new_r][new_c] != ans[k]:
        break
      elif k == 3:
        return 1

    # Change order of direction
    directions = directions[-1:] + directions[:-1]

  return num_of_occurrences


def xmas_extreme_puzzle_solver(puzzle):
  num_of_occurrences = 0

  # For every letter in the puzzle, check all directions for possible MMSS combinations
  for r in range(len(puzzle)):
    for c in range(len(puzzle[0])):
      if puzzle[r][c] != 'A':
        continue
      
      num_of_occurrences += find_extreme_xmas(puzzle, r, c)

  return num_of_occurrences