# day5.py

def day_5(input_text):
  print("\n**********************************************************")
  print("************************* Day 5 **************************")
  print("**********************************************************")

  sum_of_updates = correct_updates(input_text)
  print(f"The total sum of middle numbers from the correct updates is {sum_of_updates}")

  sum_of_incorrect_updates = fix_updates(input_text)
  print(f"The total sum of middle numbers from the newly updates is {sum_of_incorrect_updates}\n")


def is_update_valid(update, restrictions):
  previous = set() # set to store previously inspected pages
  for page in update: # inspect every page in the update
    if page in restrictions: # check if the page has any restrictions

      for r in restrictions[page]: # go through the current page's restrictions
        if r in previous: # check if the current restriction appeared in previous pages
          return False # return False because a previous page appeared in the restriction list
    
    previous.add(page) # add page to previous page list
  
  return True # return true becuase no pages went against the restrictions


def correct_updates(input_file_name):
  # We have to read two sections. The first tells us the correct rules for order of each page in an update.
  # A reading of 42|64 means that page 42 must appear before 64. I should store both this values in a dictionary.
  # The key will be the number on the right while the values will be the numbers on the left. This well be read as
  # page 64 must come after pafe 42. The updates are added as 18|12|93|62|42|64. When a page is read, the algorithm
  # will go to pages founf in dict[18] and see if any of these pages show up in the previous pages set. Once a page has
  # been inspected, it will be added to the previous pages set.

  # Step 1: Add page rules to a dictionary
  # Stpe 2: Iterate through each update
  # Step 3: Keep track of previously visited pages
  # Step 4: For every page that is inspected, see if it has any rescrictions in the dictionary
  # Step 5: Compare any restrictions to the previously visited pages
  # Step 6: If any restricted page appears in the visited pages, the update is invalid

  final_sum = 0
  restrictions = dict()
  # Open input file for reading
  try:
    with open(input_file_name, "r") as file:
      
      page_to_update_toggle = False
      while line := file.readline():
        if line == "\n":
          page_to_update_toggle = True
          continue
        
        # read through updates
        if page_to_update_toggle:
          update = line.strip().split(",")
          
          if is_update_valid(update, restrictions): # if the update is valid, get the middle number and add to final sum
            final_sum += int(update[len(update) // 2])

        # read through page restrictions
        else:
          key, value = line.strip().split("|")

          if key in restrictions:
            restrictions[key].append(value)
          else:
            restrictions[key] = [value]

  except IOError:
    print("Error: Could not read file " + input_file_name)
  
  return final_sum


def is_update_invalid(update, restrictions):
  invalid = False

  for i, page in enumerate(update): # inspect every page in the update
    if page in restrictions: # check if the page has any restrictions

      for j, p in enumerate(update[:i]): # go through update from begining to page
        if p in restrictions[page]: # check if current page matches the restricted page
          invalid = True

          # since a restriction has been found, move the restricted page right before the current page
          update = update[:j] + [page] + update[j:i] + update[i+1:]
          break

  return update, invalid


def fix_updates(input_file_name):
  final_sum = 0
  restrictions = dict()
  # Open input file for reading
  try:
    with open(input_file_name, "r") as file:
      
      page_to_update_toggle = False
      while line := file.readline():
        if line == "\n":
          page_to_update_toggle = True
          continue
        
        # read through updates
        if page_to_update_toggle:
          update = line.strip().split(",")
          
          update, invalid = is_update_invalid(update, restrictions)
          if invalid: # if the update is valid, get the middle number and add to final sum
            final_sum += int(update[len(update) // 2])

        # read through page restrictions
        else:
          key, value = line.strip().split("|")

          if key in restrictions:
            restrictions[key].append(value)
          else:
            restrictions[key] = [value]

  except IOError:
    print("Error: Could not read file " + input_file_name)
  
  return final_sum