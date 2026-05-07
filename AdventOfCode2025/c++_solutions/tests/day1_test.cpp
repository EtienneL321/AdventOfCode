#include <gtest/gtest.h>
#include "../c++_solutions/days.hpp"

extern int position;
extern int zeroPositionOccurences;
extern int zeroExtraPositionOccurences;
extern int startPosition;

class Day1Test : public ::testing::Test
{
protected:
  void SetUp() override
  {
    position = startPosition;
    zeroPositionOccurences = 0;
    zeroExtraPositionOccurences = 0;
  }
};

TEST_F(Day1Test, MoveLeftBasic)
{
  calculateCombination("L10");
  EXPECT_EQ(position, 40);
}

TEST_F(Day1Test, MoveRightBasic)
{
  calculateCombination("R5");
  EXPECT_EQ(position, 55);
}

TEST_F(Day1Test, MultipleMovesLeft)
{
  calculateCombination("L25");
  calculateCombination("L15");
  EXPECT_EQ(position, 10);
}

TEST_F(Day1Test, PositionWrappingOverZero)
{
  calculateCombination("L50");
  EXPECT_EQ(position, 0);
  EXPECT_EQ(zeroPositionOccurences, 1);
}

TEST_F(Day1Test, PositionWrappingPositiveToNegative)
{
  calculateCombination("L60");
  EXPECT_EQ(position, 90);
}
