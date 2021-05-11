# Create Header file list, though not needed to create the library, it is needed for IDEs 
set(HEADER_LIST "${MyCmakeProject_SOURCE_DIR}/include/mylib/my_file.hpp")

add_library(mylib SHARED my_file.cpp ${HEADER_LIST})

target_include_directories(mylib PUBLIC ../../include)


