# day7.py
from helper import read_by_line

def day_7():
  print("\n**********************************************************")
  print("************************* Day 7 **************************")
  print("**********************************************************")

  # This solution adds the || operator. To get the correct answer from part I, remove the || operator from calculate_result() and permutate_operators()
  equation_total = read_by_line("./inputs/day_7_input.txt", find_valid_equations)
  print(f"The total calibration result is {equation_total}")


def find_valid_equations(line):
  line = line.split(":")
  result = int(line[0])
  nums = list(map(int, line[1].strip().split()))

  # Get list of operator permutations
  operations = permutate_operators(len(nums)-1, [])

  for op in operations:
    if calculate_result(nums, op) == result:
      return result
  
  return 0


##
# calculate_result calculates the result of the given nums and operators list
# return the result of the calculation
# 
# Variables:
# - nums is a list of numbers to operate on
# - operators is a list of operators that will be inserted in their given order
##
def calculate_result(nums, operators):
  result = nums[0]

  for i, o in enumerate(operators):
    if o == "+":
      result += nums[i+1]
    
    elif o == "*":
      result *= nums[i+1]
    
    elif o == "|":
      result = int(str(result) + str(nums[i+1]))
  
  return result


##
# premutate_operators is a recursive function that will iterate through permutations of the valid operators
# returns a list of different permutations
#
# Variables
# - depth counts the number of layers the permutation can take
# - cur is the currently editable permutation
##
def permutate_operators(depth, cur):
  operators = ["+", "*", "|"]

  if depth == 0:
    return [cur]
  
  permutations = list()
  for o in operators:
    permutations += permutate_operators(depth - 1, cur + [o])
  
  return permutations
  
