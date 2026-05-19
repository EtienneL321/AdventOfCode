#ifndef DAY4_H
#define DAY4_H

#include <string>
#include <vector>

class Day4
{
private:
  std::vector<std::string> input;

  void part1Solution();
  void part2Solution();

public:
  explicit Day4(const std::string &fileName);
  ~Day4();

  void solve();
};

void day_4(std::string fileName);

#endif // DAY4_H
