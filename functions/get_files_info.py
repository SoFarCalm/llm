import os
import sys
from calculator.config import *


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(relative_path)

    is_permitted = True
    is_directory = True

    if directory not in os.listdir(working_directory) and directory !='.':
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        is_permitted = False
    
    if not os.path.isdir(relative_path):
        print(f'Error: "{directory}" is not a directory')
        is_directory = False
    
    directory_contents = os.listdir(relative_path)

    if is_directory and is_permitted:
        for content in directory_contents:
            content_path = relative_path + '/' + content
            try:
                print(f" - {content} file_size={os.path.getsize(content_path)} bytes, is_dir={os.path.isdir(content_path)}")
            except Exception as e:
                print("Error {e}")
    else:
        pass



#------TIPS-------#
# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator


# os.path.abspath: Get an absolute path from a relative path
# os.path.join: Join two paths together safely (handles slashes)
# .startswith: Check if a string starts with a specific substring
# os.path.isfile: Check if a path is a file