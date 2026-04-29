#include <iostream>
#include "days.hpp"
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
int zeroExtraPositionOccurences = 0;

void day_1(std::string fileName)
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 1 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  InputReader puzzle(fileName);

  position = startPosition;
  puzzle.readByLine(calculateCombination);

  std::cout << "The number of 0 occurences in the sequence is " << zeroPositionOccurences << std::endl;
  std::cout << "The number of 0 occurences using method 0x434C49434B is " << zeroExtraPositionOccurences << std::endl;
}

void calculateCombination(std::string movement)
{
  // std::cout << "movement: " << movement << "  " << position << "  ";
  char move = movement[0];
  int steps = std::stoi(movement.substr(1));

  int prevPos = position;

  if (move == 'L')
  {
    position -= steps;
  }
  else
  {
    position += steps;
  }

  zeroExtraPositionOccurences += std::abs(position / 100);

  if (position <= 0 && prevPos != 0)
  {
    zeroExtraPositionOccurences += 1;
  }

  // std::cout << "zero occurences: " << zeroExtraPositionOccurences << "  ";

  // We use 100 instead of 99 because our range is 0-99 (100 integers)
  position = (position % 100 + 100) % 100;

  if (position == 0)
  {
    zeroPositionOccurences++;
  }

  // std::cout << position << std::endl;
}
