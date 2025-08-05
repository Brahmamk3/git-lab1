#!/usr/bin/env python3

import os
import shutil

# step-1: define reports path
report_path=os.path.join(os.getcwd(),"reports")

# step-2 : checking reports dir exists or not
if not os.path.isdir(report_path):
  os.mkdir(report_path)
  print("reports directory not there and created!")
else:
  print("reports directory exists")

# Step 3: Loop through files in the current directory
for file in os.listdir(os.getcwd()):
    # Step 4: Check for .txt files (exclude directories)
    if file.endswith(".txt") and os.path.isfile(file):
        print(f"Found .txt file: {file}")
        
        # step -5 : move .txt files in reports directory
        start_path = os.path.join(os.getcwd(), file)
        end_path=os.path.join(report_path,file)
        shutil.move(start_path,end_path)
        print(file,"is moved to reports directory")