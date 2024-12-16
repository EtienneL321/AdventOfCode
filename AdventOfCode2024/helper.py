# helper.py

def read_to_list(input_file_name):
  # Storage for lists 1 and 2
  list1 = []
  list2 = []

  # Open input file for reading
  try:
    with open(input_file_name, "r") as file:

      # Iterate through each line of the input file
      while line := file.readline():
        split = line.split()

        # Store inputs in lists 1 and 2
        list1.append(int(split[0]))
        list2.append(int(split[1]))
      
  except IOError:
    print("Error: Could not read file " + input_file_name)
  
  return list1, list2

def read_to_integer_matrix(input_file_name):
  # Storage for matrix
  matrix = []

  # Open input file for reading
  try:
    with open(input_file_name, "r") as file:

      # Iterate through each line of the input file
      while line := file.readline():
        row = list(map(int, line.split()))

        # Store each row in matrix
        matrix.append(row)
      
  except IOError:
    print("Error: Could not read file " + input_file_name)
  
  return matrix

def read_to_char_matrix(input_file_name):
  # Storage for matrix
  matrix = []

  # Open input file for reading
  try:
    with open(input_file_name, "r") as file:

      # Iterate through each line of the input file
      while line := file.readline():
        row = list(line)

        if row[-1] == '\n':
          row = row[:-1]

        # Store each row in matrix
        matrix.append(row)
      
  except IOError:
    print("Error: Could not read file " + input_file_name)
  
  return matrix
