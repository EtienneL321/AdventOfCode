#include <string>
#include <fstream>

class InputReader
{
public:
  explicit InputReader(const std::string &fileName); // Constructor
  ~InputReader();                                    // Destructor

  int readByLine(std::function<void(std::string)>);
  int readBySeparator(char, std::function<void(std::string)>);

private:
  std::string fileName;
  std::ifstream file;
};