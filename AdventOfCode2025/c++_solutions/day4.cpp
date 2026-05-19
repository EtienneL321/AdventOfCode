#include <iostream>

#include "day4.hpp"
#include "../helper.hpp"

Day4::Day4(const std::string &fileName)
    : input()
{
  InputReader reader(fileName);
  input = reader.readByLineToVector();
}

Day4::~Day4()
{
}

void Day4::part1Solution()
{
  // TODO: Implement part 1
}

void Day4::part2Solution()
{
  // TODO: Implement part 2
}

void Day4::solve()
{
  std::cout << "\n**********************************************************" << std::endl;
  std::cout << "************************* Day 4 **************************" << std::endl;
  std::cout << "**********************************************************" << std::endl;

  part1Solution();
  part2Solution();

  std::cout << "Part 1 solution is " << "placeholder" << std::endl;
  std::cout << "Part 2 solution is " << "placeholder" << std::endl;
}

void day_4(std::string fileName)
{
  Day4 solution(fileName);
  solution.solve();
}
