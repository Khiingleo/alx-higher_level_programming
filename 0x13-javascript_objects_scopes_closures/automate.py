#!/usr/bin/python3

import os
import stat

directory_path = "/home/vagrant/alx-higher_level_programming/0x13-javascript_objects_scopes_closures"

for filename in os.listdir(directory_path):
    if filename.endswith(".js"):
        file_path = os.path.join(directory_path, filename)

        current_permissions = os.stat(file_path).st_mode

        new_permissions = current_permissions | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH

        os.chmod(file_path, new_permissions)

        print(f"made '{filename}' executable.") 
