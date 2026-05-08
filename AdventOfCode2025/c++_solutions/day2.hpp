#ifndef DAY2_H
#define DAY2_H

#include <string>
#include <vector>

class Day2
{
public:
  explicit Day2(const std::string &fileName);

  void solve();

  long long getSumOfInvalidIds() const;
  long long getSumOfInvalidXIds() const;

private:
  void invalidId(const std::string &ids);
  bool repeatedSequence(const std::string &id);
  bool repeatedXSequence(const std::string &id);

  std::vector<std::string> input;
  long long sumOfInvalidIds;
  long long sumOfInvalidXIds;
};

#endif // DAY2_H