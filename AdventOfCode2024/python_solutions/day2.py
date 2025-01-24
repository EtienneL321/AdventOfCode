# day2.py
from helper import read_by_line

def day_2(input_text):
  print("\n**********************************************************")
  print("************************* Day 2 **************************")
  print("**********************************************************")

  safe_score = read_by_line(input_text, calculate_safe_report_count)
  print(f"There are a total of {safe_score} safe reports.")

  second_safe_score = read_by_line(input_text, calculate_safe_report_count_with_removal)
  print(f"There are now a total of {second_safe_score} safe reports with removal.\n")


def is_report_safe(report):
  max_dif = 0
  min_dif = 0
  # descending
  if report[0] > report[1]:
    max_dif = -1
    min_dif = -3
  # ascending
  else:
    max_dif = 3
    min_dif = 1

  for i in range(1, len(report)):
    dif = report[i] - report[i-1]

    if dif > max_dif or dif < min_dif:
      return False, i
  
  return True, -1

def calculate_safe_report_count(report):
  # Step 1: iterate through reports in report_matrix
  # Step 2: iterate through levels of each report
  # Step 3: ensure ascending or descending order and jump between levels is not too great
  report = list(map(int, report.split(" ")))

  if is_report_safe(report)[0]:
      return 1

  return 0


def calculate_safe_report_count_with_removal(report):
  # Step 1: iterate through reports in report_matrix
  # Step 2: iterate through levels of each report
  # Step 3: ensure ascending or descending order and jump between levels is not too great
  report = list(map(int, report.split(" ")))

  check, index = is_report_safe(report)
  if check:
    return 1
  else:
      # We need to do three extra checks
      # Given a non-safe report, there is no telling which of the two levels that were compared could be removed to 
      # resolve the error. Therefore both need to be tested.
      #
      # There is an edge case where the order of the levels can flip if the first level of the report is removed. This
      # is only possible when our index is at 2 since checking the that order and step of levels 0 and 1 are correct
      # is not enough to guarantee that all future levels will require the same order.
    if is_report_safe(report[:index-1] + report[index:])[0] or is_report_safe(report[:index] + report[index+1:])[0]:
      return 1
    elif index == 2 and is_report_safe(report[1:])[0]:
      return 1

  return 0