#!/bin/bash
python_file_count=$(find . -type f -name '*.py' | wc -l)
sed -i "s/{{ PYTHON_FILE_COUNT }}/$python_file_count/g" README.md

java_file_count=$(find . -type f -name '*.java' | wc -l)
sed -i "s/{{ JAVA_FILE_COUNT }}/$java_file_count/g" README.md

c_file_count=$(find . -type f -name '*.c' | wc -l)
sed -i "s/{{ C_FILE_COUNT }}/$c_file_count/g" README.md
