#!/bin/bash

rm README.md

# Count the number of Python files
python_file_count=$(find . -type f -name '*.py' | wc -l)

# Count the number of Java files
java_file_count=$(find . -type f -name '*.java' | wc -l)

# Count the number of C files
js_file_count=$(find . -type f -name '*.js' | wc -l)

cat <<EOF > README.md
# NepsAcademy
# https://neps.academy/br/exercises 
# Resolução dos exercicios em Python, Java e JavaScript No momento estou resolvendo apenas em Python.
# Exercícios resolvidos em Python : $python_file_count
# Exercícios resolvidos em Java : $java_file_count
# Exercícios resolvidos em JavaScript : $js_file_count
EOF
