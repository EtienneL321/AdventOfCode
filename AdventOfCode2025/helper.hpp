#include <string>
#include <fstream>

class InputReader
{
public:
  explicit InputReader(const std::string &fileName); // Constructor
  ~InputReader();                                    // Destructor

  int ReadByLine(std::function<void(std::string)>);
  int ReadBySeparator(char, std::function<void(std::string)>);

private:
  std::string fileName;
  std::ifstream file;
};