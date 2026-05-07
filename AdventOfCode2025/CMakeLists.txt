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