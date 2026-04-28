#include <iostream>
#include "days.h"
#include "../helper.hpp"

void calculateCombination(std::string);

void day_2(std::string fileName)
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 2 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  InputReader puzzle(fileName);

  puzzle.ReadByLine(calculateCombination);

  // std::cout << "The number of 0 occurences in the sequence is " << zeroPositionOccurences << std::endl;
  // std::cout << "The number of 0 occurences using method 0x434C49434B is " << zeroExtraPositionOccurences << std::endl;
}

void calculateCombination(std::string movement)
{
}