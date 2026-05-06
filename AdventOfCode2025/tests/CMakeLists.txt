add_executable(aoc_tests
  day1_test.cpp
)

target_link_libraries(aoc_tests
  PRIVATE
    gtest_main
    c++_solutions
    helper
)

add_test(NAME AdventOfCode2025C++Day1Tests COMMAND aoc_tests)
