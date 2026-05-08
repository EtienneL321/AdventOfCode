#include <filesystem>
#include <gtest/gtest.h>
#include "../day1.hpp"

class Day1Test : public ::testing::Test
{
protected:
  static std::string getTestInputPath()
  {
    std::__fs::filesystem::path sourcePath = __FILE__;
    return (sourcePath.parent_path() / ".." / ".." / "puzzle_inputs" / "day_1_test_input.txt").lexically_normal().string();
  }

  Day1Test() : solver(getTestInputPath()) {}

  Day1 solver;
};

TEST_F(Day1Test, MoveLeftBasic)
{
  solver.resetPosition();
  solver.resetCounters();
  solver.calculatePart1("L10");
  EXPECT_EQ(solver.getPosition(), 40);
}

TEST_F(Day1Test, MoveRightBasic)
{
  solver.resetPosition();
  solver.resetCounters();
  solver.calculatePart1("R5");
  EXPECT_EQ(solver.getPosition(), 55);
}

TEST_F(Day1Test, MultipleMovesLeft)
{
  solver.resetPosition();
  solver.resetCounters();
  solver.calculatePart1("L25");
  solver.calculatePart1("L15");
  EXPECT_EQ(solver.getPosition(), 10);
}

TEST_F(Day1Test, PositionWrappingOverZero)
{
  solver.resetPosition();
  solver.resetCounters();
  solver.calculatePart1("L50");
  EXPECT_EQ(solver.getPosition(), 0);
  EXPECT_EQ(solver.getZeroPositionOccurences(), 1);
}

TEST_F(Day1Test, PositionWrappingPositiveToNegative)
{
  solver.resetPosition();
  solver.resetCounters();
  solver.calculatePart1("L60");
  EXPECT_EQ(solver.getPosition(), 90);
  EXPECT_EQ(solver.getZeroPositionOccurences(), 0);
}

TEST_F(Day1Test, LongInput)
{
  solver.resetPosition();
  solver.resetCounters();

  for (const auto &movement : solver.getInput())
  {
    solver.calculatePart1(movement);
  }

  EXPECT_EQ(solver.getPosition(), 32);
  EXPECT_EQ(solver.getZeroPositionOccurences(), 3);
}
