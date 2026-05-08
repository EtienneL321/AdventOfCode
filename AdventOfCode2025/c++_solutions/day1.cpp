#include <iostream>
#include <vector>

#include "day1.hpp"
#include "../helper.hpp"

Day1::Day1(const std::string &fileName)
    : startPosition(50), position(startPosition),
      zeroPositionOccurences(0), zeroExtraPositionOccurences(0)
{
  InputReader reader(fileName);
  input = reader.readByLineToVector();
}

void Day1::solve()
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 1 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  // We loop outside the solution functions vor easier testing
  position = startPosition;
  for (const auto &movement : input)
  {
    calculatePart1(movement);
  }

  position = startPosition;
  for (const auto &movement : input)
  {
    calculatePart2(movement);
  }

  std::cout << "The number of 0 occurences in the sequence is " << zeroPositionOccurences << std::endl;
  std::cout << "The number of 0 occurences using method 0x434C49434B is " << zeroExtraPositionOccurences << std::endl;
}

std::vector<std::string> Day1::getInput() const { return input; }

int Day1::getPosition() const { return position; }

int Day1::getZeroPositionOccurences() const { return zeroPositionOccurences; }

int Day1::getZeroExtraPositionOccurences() const { return zeroExtraPositionOccurences; }

void Day1::resetPosition() { position = startPosition; }

void Day1::resetCounters()
{
  zeroPositionOccurences = 0;
  zeroExtraPositionOccurences = 0;
}

void Day1::calculatePart1(const std::string &movement)
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

  position = (position % 100 + 100) % 100;

  if (position == 0)
  {
    zeroPositionOccurences++;
  }
}

void Day1::calculatePart2(const std::string &movement)
{
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

  position = (position % 100 + 100) % 100;
}

void day_1(std::string fileName)
{
  Day1 solution(fileName);
  solution.solve();
}
