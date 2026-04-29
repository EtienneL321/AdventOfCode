#include <iostream>
#include <sstream>
#include <vector>
#include "days.h"
#include "../helper.hpp"

void invalidId(std::string);
bool repeatedSequence(std::string);

// class InvalidIdPuzzle : public InputReader
// {
// public:
//   InvalidIdPuzzle(const std::string &filename)
//       : InputReader(filename), sumOfInvalidIds(0)
//   {
//   }
//   ~InvalidIdPuzzle() {};

//   void invalidId(std::string);

//   int getSumOfInvalidIds()
//   {
//     return sumOfInvalidIds;
//   };

// private:
//   int sumOfInvalidIds;
// };

long long sumOfInvalidIds = 0;

void day_2(std::string fileName)
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 2 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  char separator = ',';
  InputReader puzzle(fileName);

  puzzle.readBySeparator(separator, invalidId);

  std::cout << "The sum of invalid ids is " << sumOfInvalidIds << std::endl;
  // std::cout << "The number of 0 occurences using method 0x434C49434B is " << zeroExtraPositionOccurences << std::endl;
}

void invalidId(std::string ids)
{
  // Step 1: Split ids
  // Step 2: Remove any odd numbered ids
  // Step 3: Check for invalid ID with remainder
  std::vector<std::string> parsedIDs;
  std::istringstream tokenStream(ids);
  std::string token;
  while (std::getline(tokenStream, token, '-'))
  {
    parsedIDs.push_back(token);
  }
  long long start = std::stoll(parsedIDs[0]);
  long long end = std::stoll(parsedIDs[1]);

  while (start <= end)
  {
    std::string id = std::to_string(start);
    if (id.length() % 2 == 0 && repeatedSequence(id))
    {
      sumOfInvalidIds += std::stoll(id);
    }
    start++;
  }
}

bool repeatedSequence(std::string id)
{
  int mid = id.length() / 2;
  int start = 0;
  while (mid < id.length())
  {
    if (id[start] != id[mid])
    {
      return false;
    }
    start++;
    mid++;
  }
  return true;
}