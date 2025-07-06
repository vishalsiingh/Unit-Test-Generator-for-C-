#!/bin/bash

# Clean previous build and coverage files
rm -f *.gcda *.gcno *.gcov test_exec
find . -name "*.gcda" -delete
find . -name "*.gcno" -delete
find . -name "*.gcov" -delete

# Collect all .cpp files recursively
SRC_FILES=$(find cpp_project -name "*.cpp")
TEST_FILES=$(find tests -name "*.cpp")

# Compile with coverage flags
g++ -fprofile-arcs -ftest-coverage -g \
    $SRC_FILES $TEST_FILES \
    googletest/googletest/src/gtest-all.cc \
    -Igoogletest/googletest/include \
    -Igoogletest/googletest \
    -Icpp_project \
    -pthread \
    -o test_exec

# Run the compiled test binary
./test_exec

# Generate coverage report
for file in $SRC_FILES; do
    gcov $file
done
