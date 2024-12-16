# day1.py
from helper import read_to_list

def day_1():
  print("\n**********************************************************")
  print("************************* Day 1 **************************")
  print("**********************************************************")
  
  list1, list2 = read_to_list("./inputs/day_1_input.txt")

  distance = location_id_distance(list1, list2)
  print(f"Distance between location ids is: {distance}")

  similarity_score = calculate_similarity_score(list1, list2)
  print(f"Similarity score between lists 1 and 2 is: {similarity_score}\n")


def location_id_distance(list1, list2):
  # Sort through both lists
  list1.sort()
  list2.sort()

  # Calculate different between both lists
  total_dif = 0
  for i in range(len(list1)):
    dif = list1[i] - list2[i]

    # Check for negative distance
    if dif < 0:
      dif *= -1
  
    total_dif += dif

  return total_dif

def calculate_similarity_score(list1, list2):
  # Step 1: create a dictionary with all unique inputs from list2
  # Step 2: iterate through list1 and add to dictionary if id matches

  d = dict()
  for id in list2:
    if id not in d:
      d[id] = 1
    else:
      d[id] += 1
  
  # Get similarity score
  sim_score = 0
  for id in list1:
    if id in d:
      sim_score += (id * d[id])
  
  return sim_score