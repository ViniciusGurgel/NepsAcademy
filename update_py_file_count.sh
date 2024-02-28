#!/bin/bash

rm README.md

# Count the number of Python files
python_file_count=$(find . -type f -name '*.py' | wc -l)

# Count the number of Java files
java_file_count=$(find . -type f -name '*.java' | wc -l)

# Count the number of C files
c_file_count=$(find . -type f -name '*.c' | wc -l)

cat <<EOF > README.md
# NepsAcademy
# https://neps.academy/br/exercises 
# Resolução dos exercicios em Python, Java e C No momento estou resolvendo apenas em Python.
# Exercícios resolvidos em Python : $python_file_count
# Exercícios resolvidos em Java : $java_file_count
# Exercícios resolvidos em C : $c_file_count
EOF
