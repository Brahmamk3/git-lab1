#!/usr/bin/env python3

# List only .txt files in the current directory.

import os

current_directory=os.getcwd()

for file in os.listdir(current_directory):
  if file.endswith(".txt") and os.path.isfile(file):
    print(file)