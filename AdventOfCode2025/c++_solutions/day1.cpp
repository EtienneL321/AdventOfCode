#include <iostream>
#include "days.h"
#include "../helper.hpp"

// class Combination : public InputReader
// {
// public:
//   Combination(const std::string &filename)
//       : InputReader(filename), zeroPositionOccurences(0), position(50)
//   {
//   }
//   ~Combination() {};

//   void calculateCombination();

//   int getZeroPositionOccurences()
//   {
//     return zeroPositionOccurences;
//   };

// private:
//   int position;
//   int zeroPositionOccurences;
// };

void calculateCombination(std::string);

int startPosition = 50;
int position = startPosition;
int zeroPositionOccurences = 0;

void day_1()
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 1 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  std::string test_file = "./AdventOfCode2025/puzzle_inputs/day_1_test_input.txt";
  std::string real_file = "./AdventOfCode2025/puzzle_inputs/day_1_input.txt";

  InputReader puzzle(test_file);

  position = startPosition;
  puzzle.ReadByLine(calculateCombination);

  std::cout << "The number of 0 occurences in the sequence is " << zeroPositionOccurences << "." << std::endl;
}

void calculateCombination(std::string movement)
{
  char move = movement[0];
  int steps = std::stoi(movement.substr(1));

  if (move == 'L')
  {
    position -= steps;
  }
  else
  {
    position += steps;
  }

  // We use 100 instead of 99 because our range is 0-99 (100 integers)
  position %= 100;

  if (position == 0)
  {
    zeroPositionOccurences++;
  }
}
