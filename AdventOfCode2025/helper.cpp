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

std::vector<std::string> InputReader::readByLineToVector()
{
  std::vector<std::string> lines;

  if (!file.is_open())
  {
    std::cerr << "Error: could not open file " << fileName << "." << std::endl;
    return lines;
  }

  std::string line;
  while (std::getline(file, line))
  {
    lines.push_back(line);
  }

  return lines;
}

std::vector<std::string> InputReader::readBySeparatorToVector(char separator)
{
  std::vector<std::string> tokens;

  if (!file.is_open())
  {
    std::cerr << "Error: could not open file " << fileName << "." << std::endl;
    return tokens;
  }

  std::string line;
  std::getline(file, line);
  std::istringstream tokenStream(line);

  std::string value;
  while (std::getline(tokenStream, value, separator))
  {
    tokens.push_back(value);
  }

  return tokens;
}

std::vector<std::vector<std::string>> InputReader::readGrid()
{
  std::vector<std::vector<std::string>> grid;

  if (!file.is_open())
  {
    std::cerr << "Error: could not open file " << fileName << "." << std::endl;
    return grid;
  }

  std::string row;
  while (std::getline(file, row))
  {
    std::vector<std::string> line;
    for (auto &col : row)
    {
      line.push_back(std::string(1, col));
    }
    grid.push_back(line);
  }

  return grid;
}