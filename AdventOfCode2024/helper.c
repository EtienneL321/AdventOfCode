#include <stdio.h>

/**
 * This function reads a list of integers from a file and stores them in an array.
 *
 * Arguemnts:
 * - filename: The name of the file to read from.
 * - list1: The array to store the first column of integers.
 * - list2: The array to store the second column of integers
 * - size: A pointer to an integer to store the size of the list.
 *
 * Returns:
 * - int: 0 if the operation was successful
 */
int read_to_list(char *filename, int *list1, int *list2, int *size)
{
  FILE *file = fopen(filename, "r");
  if (file == NULL)
  {
    printf("Error: Unable to open file %s\n", filename);
    return 1;
  }

  int i = 0;
  while (fscanf(file, "%d %d", &list1[i], &list2[i]) != EOF)
  {
    i++;
  }
  *size = i;

  fclose(file);

  return 0;
}

int compare(const void *a, const void *b)
{
  return (*(int *)a - *(int *)b);
}