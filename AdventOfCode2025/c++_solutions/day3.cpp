#include <iostream>
#include <algorithm>
#include <cmath>
#include "days.hpp"
#include "../helper.hpp"

void calculateJoltageSum(std::string);
void largestTwoJoltage(std::string);
void largestTwelveJoltage(std::string);

long sumOfTwoJoltage = 0;
long long sumOfTwelveJoltage = 0;
int numOfCells = 12;

void day_3(std::string fileName)
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 3 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  InputReader puzzle(fileName);

  puzzle.readByLine(calculateJoltageSum);

  std::cout << "The sum of two joltages is " << sumOfTwoJoltage << std::endl;
  std::cout << "The sum of twelve joltages is " << sumOfTwelveJoltage << std::endl;
}

void calculateJoltageSum(std::string bank)
{
  largestTwoJoltage(bank);
  largestTwelveJoltage(bank);
}

void largestTwoJoltage(std::string bank)
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

  sumOfTwoJoltage += (leftNum * 10) + rightNum;
}

void largestTwelveJoltage(std::string bank)
{
  // Rather than us a sliding window, we will calculate the best cell to activate one at a time
  int leftBound = 0;
  int rightBound = bank.length() - numOfCells;
  long long sum = 0;

  // We need twelve cells so the rightBound is used to get us the largest output up to the max
  // index the cell can occupy
  // Example: 1  2  3  4  5  6  7  8  9  1  1  1  1  1  1
  // Indeces: 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
  // Explanation: As we look for our first cell, even though 9 is the largest output, the max index
  // it can occupy is up to index 3 (15-12)

  // Outer loop will iterate at most 12 times to find our 12 cells
  // Inner loop moves left to right and keeps track of the cell with the largest output
  for (int i = numOfCells; i > 0; i--)
  {
    int largestNum = bank[leftBound] - '0';
    for (int j = leftBound + 1; j <= rightBound; j++)
    {
      if (bank[j] - '0' > largestNum)
      {
        largestNum = bank[j] - '0';
        leftBound = j;
      }
    }
    sum += (largestNum * std::pow(10, i - 1));

    rightBound++;
    leftBound++;
  }

  sumOfTwelveJoltage += sum;
}