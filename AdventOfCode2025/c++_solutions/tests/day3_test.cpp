#include <gtest/gtest.h>
#include "../c++_solutions/days.hpp"

extern long sumOfJoltage;

class Day3Test : public ::testing::Test
{
protected:
  void SetUp() override
  {
    sumOfJoltage = 0;
  }
};

TEST_F(Day3Test, descendingOrderAtStart)
{
  largestJoltage("987654321");
  EXPECT_EQ(sumOfJoltage, 98);
}

TEST_F(Day3Test, largestIntegerAtEnd)
{
  largestJoltage("81818189");
  EXPECT_EQ(sumOfJoltage, 89);
}

TEST_F(Day3Test, largestIntegersAtEnd)
{
  largestJoltage("818181899");
  EXPECT_EQ(sumOfJoltage, 99);
}

TEST_F(Day3Test, repeatPattern)
{
  largestJoltage("818181");
  EXPECT_EQ(sumOfJoltage, 88);
}

TEST_F(Day3Test, largestIntegerInMiddle)
{
  largestJoltage("111111211");
  EXPECT_EQ(sumOfJoltage, 21);
}

TEST_F(Day3Test, sameIntegers)
{
  largestJoltage("111111111");
  EXPECT_EQ(sumOfJoltage, 11);
}

TEST_F(Day3Test, onlyMoveRightPointer)
{
  largestJoltage("9111112113111");
  EXPECT_EQ(sumOfJoltage, 93);
}

TEST_F(Day3Test, solutionFromStart)
{
  largestJoltage("99111112113111");
  EXPECT_EQ(sumOfJoltage, 99);
}

TEST_F(Day3Test, solutionFromStart2)
{
  largestJoltage("4321");
  EXPECT_EQ(sumOfJoltage, 43);
}

TEST_F(Day3Test, largeInput)
{
  largestJoltage("3232332132231233321122322231333232213233313332432312143232132213233232233243131223222222233422123252");
  EXPECT_EQ(sumOfJoltage, 52);
}

TEST_F(Day3Test, largeInput2)
{
  largestJoltage("3222222222222222246212321331121322212122262252122223122222121222232222222221223222222212222222533232");
  EXPECT_EQ(sumOfJoltage, 66);
}

TEST_F(Day3Test, ascendingWithEvenNumber)
{
  largestJoltage("1231");
  EXPECT_EQ(sumOfJoltage, 31);
}

TEST_F(Day3Test, ascendingWithOddNumber)
{
  largestJoltage("12231");
  EXPECT_EQ(sumOfJoltage, 31);
}