# day8.py
from helper import read_to_char_matrix

def day_8(input_text):
  print("\n**********************************************************")
  print("************************* Day 8 **************************")
  print("**********************************************************")

  matrix = read_to_char_matrix(input_text)
  antinodes = unique_antinodes(matrix)
  print(f"The number of unique antinodes is {antinodes}")

  resonant_antinodes = unique_resonant_antinodes(matrix)
  print(f"The number of unique resonant antinodes is {resonant_antinodes}\n")

##
# in_bounds checks if the given row and column are within the bounds of the matrix
#
# Variables:
# - n_row is the number of rows in the matrix
# - n_col is the number of columns in the matrix
# - row is the row to check
# - col is the column to check
#
# Returns True if the row and column are within the bounds of the matrix, False otherwise
##
def in_bounds(n_row, n_col, row, col):
  return 0 <= row < n_row and 0 <= col < n_col

##
# unique_antinodes finds the number of unique antinodes in the given matrix.
# 
# Variables:
# - matrix is the given matrix
#
# Returns the number of unique antinodes
##
def unique_antinodes(matrix):
  antennas = dict()
  antinodes = set()

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      c = matrix[i][j]
      if c != ".":
        if c not in antennas:
          antennas[c] = [(i, j)]
        else:
          antennas[c].append((i, j))
  
  for pairs in antennas.values():
    for i in range(len(pairs)):
      for j in range(i+1, len(pairs)):
        dif = (pairs[i][0] - pairs[j][0], pairs[i][1] - pairs[j][1])
        
        antinode = (pairs[i][0] + dif[0], pairs[i][1] + dif[1])
        if in_bounds(len(matrix), len(matrix[0]), antinode[0], antinode[1]):
          antinodes.add(antinode)
        
        antinode = (pairs[j][0] - dif[0], pairs[j][1] - dif[1])
        if in_bounds(len(matrix), len(matrix[0]), antinode[0], antinode[1]):
          antinodes.add(antinode)
  
  return len(antinodes)

##
# unique_resonant_antinodes finds the number of unique resonant antinodes in the given matrix.
#
# Variables:
# - matrix is the given matrix
#
# Returns the number of unique resonant antinodes
##
def unique_resonant_antinodes(matrix):
  antennas = dict()
  antinodes = set()

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      c = matrix[i][j]
      if c != ".":
        if c not in antennas:
          antennas[c] = [(i, j)]
        else:
          antennas[c].append((i, j))

        antinodes.add((i, j))        
  
  for pairs in antennas.values():
    for i in range(len(pairs)):
      for j in range(i+1, len(pairs)):
        dif = (pairs[i][0] - pairs[j][0], pairs[i][1] - pairs[j][1])
        
        # Only difference from the first implementation is we want to iterate until our antinode is out of bounds
        left = pairs[i]
        while(True):
          antinode = (left[0] + dif[0], left[1] + dif[1])
          if not in_bounds(len(matrix), len(matrix[0]), antinode[0], antinode[1]):
            break

          # if antinode not in antinodes:
          antinodes.add(antinode)
          
          left = antinode
        
        right = pairs[j]
        while(True):
          antinode = (right[0] - dif[0], right[1] - dif[1])
          if not in_bounds(len(matrix), len(matrix[0]), antinode[0], antinode[1]):
            break

          # if antinode not in antinodes:
          antinodes.add(antinode)
          
          right = antinode

  return len(antinodes)