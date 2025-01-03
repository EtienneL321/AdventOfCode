#include <stdio.h>
#include <stdlib.h>

#include "helper.h"
#include "hashtable.h"

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

  // for (int i = 0; i < size; i++)
  // {
  //   printf("Values at %d is: %d and %d\n", i, list1[i], list2[i]);
  // }

  Hashtable map;

  initialize_hashtable(&map);

  add_to_hashtable(&map, "sport");
  add_to_hashtable(&map, "Sport");
  add_to_hashtable(&map, "sport");
  add_to_hashtable(&map, "train");
  add_to_hashtable(&map, "Hello World!");
  add_to_hashtable(&map, "Hello World!");
  add_to_hashtable(&map, "Hello World!");
  add_to_hashtable(&map, "Hello World!");
  add_to_hashtable(&map, "Hello World!");
  add_to_hashtable(&map, "Hello World!");
  add_to_hashtable(&map, "Hello World");

  print_hashtable(&map);

  char *key = "Hello World!";
  int n = search_hashtable(&map, key);
  if (n != -1)
  {
    printf("Key \"%s\" has a value of %d\n", key, n);
  }

  /**
   * An intersting bug occurs here where just inputing the string "Hello World" as the
   * input causes a "No key found error" even if the key "Hello World" can be found.
   * This is probably caused by a key of type char * being different than the default type
   * given to the c string "Hello World".
   */
  int c = search_hashtable(&map, (char *)"Hello world");

  key = "sport";
  remove_from_hashtable(&map, key);
  // print_hashtable(&map);

  add_to_hashtable(&map, "tree");
  add_to_hashtable(&map, "Francais");
  add_to_hashtable(&map, "Fourmi");
  add_to_hashtable(&map, "Joe Dassin");
  add_to_hashtable(&map, "Duran Duran");
  add_to_hashtable(&map, "Queen");
  add_to_hashtable(&map, "View to a Kill");
  // add_to_hashtable(&map, "Rio");
  // add_to_hashtable(&map, "Hungry");

  print_hashtable(&map);

  free_hashtable(&map);
  printf("\n");
  return 0;
}