#include <stdio.h>
#include <stdlib.h>

#include "helper.h"

int calculate_distance(int *list1, int *list2, int size)
{
  int total_distance = 0;

  for (int i = 0; i < size; i++)
  {
    total_distance += abs(list1[i] - list2[i]);
  }

  return total_distance;
}

int main()
{
  printf("\n");

  int list1[1000];
  int list2[1000];
  int size;

  char *filename = "./AdventOfCode2024/puzzle_inputs/day_1_input.txt";

  // Read file to two lists
  if (read_to_list(filename, list1, list2, &size))
  {
    fprintf(stderr, "Day 1 input text could not be read");
  }

  // Sort lists
  qsort(list1, size, sizeof(int), compare);
  qsort(list2, size, sizeof(int), compare);

  // Calculate distance between two lists
  int distance = calculate_distance(list1, list2, size);

  printf("The total distance between both lists is %d\n", distance);

  return 0;
}