#!/usr/bin/python3

import os
import shutil

main_folder = "main"
if not os.path.exists(main_folder):
    os.makedirs(main_folder)


current_directory = os.getcwd()
files = os.listdir(current_directory)

for file in files:
    if file.endswith("main.js"):
        file_path = os.path.join(current_directory, file)
        shutil.move(file_path, os.path.join(main_folder, file))

print("moved files ending with 'main.js' to 'main' folder.")
