#!/usr/bin/env python3

# List only .txt files in the current directory.

import os

current_directory=os.getcwd()

for file in os.listdir(current_directory):
  if file.endswith(".txt") and os.path.isfile(file):
    print(file)


""" 
output:
brahm@Brahmanjaneyulu MINGW64 /c/Devops-45days/YAML/git-lab-1 (master)
$ python question4.py 
file.txt
"""