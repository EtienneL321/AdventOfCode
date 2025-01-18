# day9.py
from helper import read_by_line

def day_9(input_text):
  print("\n**********************************************************")
  print("************************* Day 9 **************************")
  print("**********************************************************")

  checksum = read_by_line(input_text, calculate_filesystem_checksum)
  print(f"The checksum of the first filesystem is {checksum}\n")

##
# unravel_disk_map unravels the code it is given into a series of file space and free space
#
# Variables:
# - line is the input line that will be unraveled
# Returns:
# - disk_map is a list of the disk space and free space
##
def unravel_disk_map(line):
  space_toggle = True # When true, allocate memory for the disk map, when false, add free space
  disk_map = []
  pos = 0

  for n in line:
    if n == "\n": # This statement is needed to process large inputs
      continue
      
    for _ in range(int(n)):
      if space_toggle:
        disk_map.append(pos)
      else:
        disk_map.append(".")
    
    if space_toggle:
      pos += 1
    space_toggle = not space_toggle

  return disk_map


##
# move_blocks moves the blocks from right to left in the disk map until there is one block of contiguous data
#
# Variables:
# - disk_map is the disk map that will be manipulated
#
# Returns:
# - disk_map is the modified disk map
##
def move_blocks(disk_map):
  left = 0
  right = len(disk_map) - 1

  while left < right:
    if disk_map[left] != ".":
      left += 1
    
    if disk_map[right] == ".":
      right -= 1
    
    if disk_map[left] == "." and disk_map[right] != ".":
      disk_map[left], disk_map[right] = disk_map[right], disk_map[left]
      left += 1
      right -= 1
    
  return disk_map
  

def calculate_filesystem_checksum(line):
  disk_map = unravel_disk_map(line)

  disk_map = move_blocks(disk_map)

  checksum = 0
  i = 0
  while disk_map[i] != ".":
    checksum += (i * int(disk_map[i]))
    i += 1 
  
  return checksum