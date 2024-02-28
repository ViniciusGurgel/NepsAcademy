#!/bin/bash

# Count .py files in the repository
file_count=$(find . -type f -name '*.py' | wc -l)

# Update README file with the file count
sed -i "s/{{ FILE_COUNT }}/$file_count/g" README.md
