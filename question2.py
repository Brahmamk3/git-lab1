#!/usr/bin/env python3
#Q2: Check if a Path is a File or Directory

import os

path =input("enter file or directory path:")

if os.path.isfile(path):
  print("file exists")
elif os.path.isdir(path):
  print("directory exists")
else:
  print("file or directory not exists")

""" 
output:
brahm@Brahmanjaneyulu MINGW64 /c/Devops-45days/YAML/git-lab-1 (master)
$ python question2.py 
enter file or directory path:question1.py
path exists

"""
