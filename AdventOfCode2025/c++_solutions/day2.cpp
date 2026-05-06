#include <iostream>
#include <sstream>
#include <vector>
#include "days.hpp"
#include "../helper.hpp"

void invalidId(std::string);
bool repeatedSequence(std::string);
bool repeatedXSequence(std::string);

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
long long sumOfInvalidXIds = 0;

void day_2(std::string fileName)
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 2 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  char separator = ',';
  InputReader puzzle(fileName);

  puzzle.readBySeparator(separator, invalidId);

  std::cout << "The sum of invalid ids with twice repeated patterns is " << sumOfInvalidIds << std::endl;
  std::cout << "The sum of invalid ids with multiple repeated patterms is " << sumOfInvalidXIds << std::endl;
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
    // First solution
    if (id.length() % 2 == 0 && repeatedSequence(id))
    {
      sumOfInvalidIds += std::stoll(id);
    }

    // Second solution
    if (repeatedXSequence(id))
    {
      sumOfInvalidXIds += std::stoll(id);
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

bool repeatedXSequence(std::string id)
{
  if (id.length() == 1)
  {
    // id cannot have a repeated sequence
    return false;
  }

  // Create substrings until halfway through
  std::string sub = std::to_string(id[0]); // first substring to test
  int mid = id.length() / 2;               // middle index of id

  while (sub.length() <= mid)
  {
    // Step 1: Check if id is divisible by substring length
    if (id.length() % sub.length() != 0)
    {
      sub += id[sub.length() + 1];
      continue;
    }

    // Step 2: Check if this substring creates a pattern
    // First loop jumps every substring length
    for (int i = 0; i < id.length(); i += sub.length())
    {
      // Second loop checks that the current string matches the substring
      for (int j = i; j < i + sub.length(); j++)
      {
        // No match means the substring is not repeated
        if (id[j] != sub[j - i])
        {
          continue;
        }
      }
    }

    // Step 3: If we made it past the double for loop, that means out substring was repeated
    return true;
  }

  return false;
}