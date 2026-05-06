cmake_minimum_required(VERSION 3.31)
set(CMAKE_CXX_STANDARD 11)

project(AdventOfCode2025)

enable_testing()
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_executable(main_cpp)
target_sources(main_cpp
  PRIVATE
    main.cpp
)
target_link_libraries(main_cpp
  PRIVATE
    helper
    c++_solutions
)

add_library(helper)
target_sources(helper
  PRIVATE
    helper.cpp
  
  PUBLIC
    FILE_SET HEADERS
    FILES
      helper.hpp
)

add_subdirectory(c++_solutions)
add_subdirectory(tests)