#include <iostream>
#include <sstream>
#include <vector>

#include "day2.hpp"
#include "../helper.hpp"

Day2::Day2(const std::string &fileName)
    : sumOfInvalidIds(0), sumOfInvalidXIds(0)
{
  InputReader reader(fileName);
  input = reader.readBySeparatorToVector(',');
}

Day2::~Day2()
{
}

void Day2::solve()
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 2 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  for (const auto &ids : input)
  {
    invalidId(ids);
  }

  std::cout << "The sum of invalid ids with twice repeated patterns is " << sumOfInvalidIds << std::endl;
  std::cout << "The sum of invalid ids with multiple repeated patterns is " << sumOfInvalidXIds << std::endl;
}

long long Day2::getSumOfInvalidIds() const
{
  return sumOfInvalidIds;
}

long long Day2::getSumOfInvalidXIds() const
{
  return sumOfInvalidXIds;
}

void Day2::invalidId(const std::string &ids)
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

bool Day2::repeatedSequence(const std::string &id)
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

bool Day2::repeatedXSequence(const std::string &id)
{
  if (id.length() == 1)
  {
    // id cannot have a repeated sequence
    return false;
  }

  // Create substrings until halfway through
  std::string sub(1, id[0]); // first substring to test
  int mid = id.length() / 2; // middle index of id

start_while_loop:
  while (sub.length() <= mid)
  {
    // Step 1: Check if id is divisible by substring length
    if (id.length() % sub.length() != 0)
    {
      sub += id[sub.length()];
      goto start_while_loop;
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
          sub += id[sub.length()];
          goto start_while_loop;
        }
      }
    }

    // Step 3: If we made it past the double for loop, that means our substring was repeated
    return true;
  }

  return false;
}

void day_2(std::string fileName)
{
  Day2 solution(fileName);
  solution.solve();
}