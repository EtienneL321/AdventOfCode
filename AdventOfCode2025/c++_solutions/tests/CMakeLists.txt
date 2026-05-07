include(GoogleTest)

add_executable(day1_tests day1_test.cpp)
target_link_libraries(day1_tests
  PRIVATE
    gtest_main
    c++_solutions
    helper
)
gtest_discover_tests(day1_tests)

add_executable(day3_tests day3_test.cpp)
target_link_libraries(day3_tests
  PRIVATE
    gtest_main
    c++_solutions
    helper
)
gtest_discover_tests(day3_tests)
