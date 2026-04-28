#include <iostream>
#include <sstream>

#include "helper.hpp"

InputReader::InputReader(const std::string &fileName) : fileName(fileName), file(fileName)
{
}

InputReader::~InputReader()
{
  this->file.close();
}

int InputReader::readByLine(std::function<void(std::string)> callback)
{
  // Check if the file open
  if (!file.is_open())
  {
    std::cerr << "Error: could not open file " << fileName << "." << std::endl;
    return 1;
  }

  std::string line;
  // Read line by line
  while (std::getline(file, line))
  {
    callback(line);
  }

  return 0;
}

int InputReader::readBySeparator(char separator, std::function<void(std::string)> callback)
{
  // Check if the file open
  if (!file.is_open())
  {
    std::cerr << "Error: could not open file " << fileName << "." << std::endl;
    return 1;
  }

  std::string line;
  std::getline(file, line);
  std::istringstream tokenStream(line);

  std::string value;
  while (std::getline(tokenStream, value, separator))
  {
    callback(value);
  }

  return 0;
}