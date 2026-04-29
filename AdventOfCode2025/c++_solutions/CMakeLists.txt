add_library(c++_solutions)

target_sources(c++_solutions
  PRIVATE
    day1.cpp
    day2.cpp
  
  PUBLIC
    FILE_SET HEADERS
    FILES
      days.hpp
)