# Example pulled in part from Henery Schreiner at:
# https://gitlab.com/CLIUtils/modern-cmake
cmake_minimum_required(VERSION 3.11...3.20)

# Project Name
project(
  MyCmakeProject
  VERSION 1.0
  DESCRIPTION "Example CMake Project"
  LANGUAGES CXX)

#ORDER HERE MATTERS!

# Explore the source file directory for library code
add_subdirectory(src)

# Explore the exectuble file directory for exec. code
add_subdirectory(apps)



