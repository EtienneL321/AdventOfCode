cmake_minimum_required(VERSION 3.31)
set(CMAKE_CXX_STANDARD 11)

project(AdventOfCode2025)

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