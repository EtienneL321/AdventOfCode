#include <string>
#include <vector>
#include <fstream>
#include <functional>

class InputReader
{
public:
  explicit InputReader(const std::string &fileName); // Constructor
  ~InputReader();                                    // Destructor

  // Deprecated
  int readByLine(std::function<void(std::string)>);
  int readBySeparator(char, std::function<void(std::string)>);

  std::vector<std::string> readByLineToVector();
  std::vector<std::string> readBySeparatorToVector(char);

private:
  std::string fileName;
  std::ifstream file;
};