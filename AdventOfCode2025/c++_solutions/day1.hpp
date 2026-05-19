#ifndef DAY1_H
#define DAY1_H

#include <string>
#include <vector>

class Day1
{
public:
  explicit Day1(const std::string &fileName);
  ~Day1();

  void solve();

  std::vector<std::string> getInput() const;
  int getPosition() const;
  int getZeroPositionOccurences() const;
  int getZeroExtraPositionOccurences() const;

  void resetPosition();
  void resetCounters();

  void calculatePart1(const std::string &movement);
  void calculatePart2(const std::string &movement);

private:
  std::vector<std::string> input;
  int startPosition;
  int position;
  int zeroPositionOccurences;
  int zeroExtraPositionOccurences;
};

#endif // DAY1_H
