# from get_files_info import get_files_info
# from get_file_content import get_file_content
# from write_file import write_file
import os
import subprocess

# def run_python_file(working_directory, file_path, args=[]):
#     abs_working_dir = os.path.abspath(working_directory)
#     relative_path = os.path.join(working_directory, file_path)
#     target = os.path.abspath(relative_path)
#     relative_contents = os.listdir(working_directory)
#     relative_contents_tuple = tuple(relative_contents)

#     if not target.startswith(abs_working_dir):
#         print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
#         return
    
#     if not file_path.startswith(relative_contents_tuple):
#         print(f'Error: File "{file_path}" not found.')
#         return
    
#     if file_path[-3:] != '.py':
#         print(f'Error: "{file_path}" is not a Python file.')
#         return
    
#     subprocess.run(["uv", "run", working_directory, file_path], timeout=30, text=True)

import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"

#------TIP-------#
# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator
# os.path.dirname: It returns the "head" of the path, which is everything leading up to the last component