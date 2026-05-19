#include <iostream>
#include <vector>

#include "c++_solutions/days.hpp"

std::string getFileName(int day, bool test)
{
  std::string fileName;
  if (test)
  {
    fileName = "./AdventOfCode2025/puzzle_inputs/day_" + std::to_string(day) + "_test_input.txt";
  }
  else
  {
    fileName = "./AdventOfCode2025/puzzle_inputs/day_" + std::to_string(day) + "_input.txt";
  }

  return fileName;
}

int main(int argc, char *argv[])
{
  if (argc < 2)
  {
    std::cout << "Wrong argument count, please include the day and optional test flag" << std::endl;
  }

  std::function<void(std::string)> dayList[4] = {day_1, day_2, day_3, day_4};

  int day = std::stoi(argv[1]);
  if (day < 1 || day > 25)
  {
    std::cout << "Inputed day was not between 1 and 25. Printing day 1 instead." << std::endl;
    day = 1;
  }

  // Store any flags in a vector
  std::vector<char> flags;
  for (int i = 2; i < argc; i++)
  {
    std::string value = argv[i];
    if (value[0] == '-' && (sizeof(value) / sizeof(value[0])) > 1)
    {
      flags.push_back(value[1]);
    }
  }

  bool testFlag = false;
  for (char &flag : flags)
  {
    if (flag == 't')
    {
      testFlag = true;
    }
  }

  std::string fileName = getFileName(day, testFlag);

  if (day > (sizeof(dayList) / sizeof(dayList[0])))
  {
    std::cout << "Input day has no solution. Printing day 1 instead." << std::endl;
    day = 1;
  }

  // offset day by 1
  day--;
  dayList[day](fileName);

  return 0;
}