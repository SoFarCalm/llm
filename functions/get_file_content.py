import os
from calculator.config import *

def get_file_content(working_directory, file_path):

    is_permitted = True
    is_file = True

    relative_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(relative_path)
    relative_contents = os.listdir(working_directory)
    relative_contents_tuple = tuple(relative_contents)

    if not file_path.startswith(relative_contents_tuple):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        is_permitted = False
    
    if not os.path.isfile(relative_path):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        is_file = False
    
    if is_file and is_permitted:
        try:
            max_limit_msg = f"[...File '{file_path}' truncated at 10000 characters]"
            with open(relative_path, "r") as f:
                file_content_string = f.read(MAX_CHAR)

                if len(file_content_string) == MAX_CHAR:
                    print(file_content_string, max_limit_msg)
                else:
                    print(file_content_string)
        except Exception as e:
            print(f"Error {e}")

# def get_file_content(working_directory, file_path):
#     abs_working_dir = os.path.abspath(working_directory)
#     abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
#     #print(abs_file_path)
#     if not abs_file_path.startswith(abs_working_dir):
#         return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
#     if not os.path.isfile(abs_file_path):
#         return f'Error: File not found or is not a regular file: "{file_path}"'
#     try:
#         with open(abs_file_path, "r") as f:
#             content = f.read(MAX_CHARS)
#             if os.path.getsize(abs_file_path) > MAX_CHARS:
#                 content += (
#                     f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
#                 )
#         return content
#     except Exception as e:
#         return f'Error reading file "{file_path}": {e}'