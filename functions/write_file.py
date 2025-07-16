import os
import sys

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, file_path)
    target = os.path.abspath(relative_path)
    relative_contents = os.listdir(working_directory)
    relative_contents_tuple = tuple(relative_contents)

    print(f"This is abs_working_dir: {abs_working_dir}")
    print(f"This is target: {target}")

    if not target.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target):
        try:
            with open(target, "w") as f:
                f.write(content)
                print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')

        except Exception as e:
            print(f"Error writing file {file_path}: {e}")