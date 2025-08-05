#!/usr/bin/env python3

#creates a folder named test_folder in the current working directory only if it doesn't already exist:

import os

folder="test_folder"

if os.path.isdir(folder):
  print("test_folder is already exists")
else:
  print("test_folder not exists")
  os.mkdir(folder)

# path=os.path.join(os.getcwd(),folder) : join folder with current path

