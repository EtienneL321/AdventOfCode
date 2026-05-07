#include <gtest/gtest.h>
#include "../c++_solutions/days.hpp"

extern long sumOfTwoJoltage;
extern long long sumOfTwelveJoltage;

class Day3Test : public ::testing::Test
{
protected:
  void SetUp() override
  {
    sumOfTwoJoltage = 0;
    sumOfTwelveJoltage = 0;
  }
};

TEST_F(Day3Test, descendingOrderAtStart)
{
  calculateJoltageSum("987654321");
  EXPECT_EQ(sumOfTwoJoltage, 98);
}

TEST_F(Day3Test, largestIntegerAtEnd)
{
  calculateJoltageSum("81818189");
  EXPECT_EQ(sumOfTwoJoltage, 89);
}

TEST_F(Day3Test, largestIntegersAtEnd)
{
  calculateJoltageSum("818181899");
  EXPECT_EQ(sumOfTwoJoltage, 99);
}

TEST_F(Day3Test, repeatPattern)
{
  calculateJoltageSum("818181");
  EXPECT_EQ(sumOfTwoJoltage, 88);
}

TEST_F(Day3Test, largestIntegerInMiddle)
{
  calculateJoltageSum("111111211");
  EXPECT_EQ(sumOfTwoJoltage, 21);
}

TEST_F(Day3Test, sameIntegers)
{
  calculateJoltageSum("111111111");
  EXPECT_EQ(sumOfTwoJoltage, 11);
}

TEST_F(Day3Test, onlyMoveRightPointer)
{
  calculateJoltageSum("9111112113111");
  EXPECT_EQ(sumOfTwoJoltage, 93);
}

TEST_F(Day3Test, solutionFromStart)
{
  calculateJoltageSum("99111112113111");
  EXPECT_EQ(sumOfTwoJoltage, 99);
}

TEST_F(Day3Test, solutionFromStart2)
{
  calculateJoltageSum("4321");
  EXPECT_EQ(sumOfTwoJoltage, 43);
}

TEST_F(Day3Test, largeInput)
{
  calculateJoltageSum("3232332132231233321122322231333232213233313332432312143232132213233232233243131223222222233422123252");
  EXPECT_EQ(sumOfTwoJoltage, 52);
}

TEST_F(Day3Test, largeInput2)
{
  calculateJoltageSum("3222222222222222246212321331121322212122262252122223122222121222232222222221223222222212222222533232");
  EXPECT_EQ(sumOfTwoJoltage, 66);
}

TEST_F(Day3Test, ascendingWithEvenNumber)
{
  calculateJoltageSum("1231");
  EXPECT_EQ(sumOfTwoJoltage, 31);
}

TEST_F(Day3Test, ascendingWithOddNumber)
{
  calculateJoltageSum("12231");
  EXPECT_EQ(sumOfTwoJoltage, 31);
}