#include <iostream>
#include <algorithm>
#include "days.hpp"
#include "../helper.hpp"

void largestJoltage(std::string);

long sumOfJoltage = 0;

void day_3(std::string fileName)
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 3 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  InputReader puzzle(fileName);

  puzzle.readByLine(largestJoltage);

  std::cout << "The sum of joltages is " << sumOfJoltage << std::endl;
}

void largestJoltage(std::string bank)
{
  int left = 0;
  int right = 1;

  int leftNum = bank[left] - '0';
  int rightNum = bank[right] - '0';

  while (right < bank.length())
  {
    // right points to a larger number than left and we are not at the end of the bank
    // this works becuase numbers are ordered in ascii
    if (bank[right] > bank[left] && (right != bank.length() - 1))
    {
      leftNum = bank[right] - '0';
      left = right;
      rightNum = bank[right + 1] - '0';
    }
    else
    {
      // right will be the max of its previous val and now
      rightNum = std::max(rightNum, bank[right] - '0');
    }

    right++;
  }

  sumOfJoltage += (leftNum * 10) + rightNum;
}