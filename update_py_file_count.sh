#!/bin/bash

# Count the number of Python files
python_file_count=$(find . -type f -name '*.py' | wc -l)

# Count the number of Java files
java_file_count=$(find . -type f -name '*.java' | wc -l)

# Count the number of C files
c_file_count=$(find . -type f -name '*.c' | wc -l)

# Replace the placeholders in README.md with the actual file counts
sed -i "s/{{ PYTHON_FILE_COUNT }}/$python_file_count/g" README.md
sed -i "s/{{ JAVA_FILE_COUNT }}/$java_file_count/g" README.md
sed -i "s/{{ C_FILE_COUNT }}/$c_file_count/g" README.md

