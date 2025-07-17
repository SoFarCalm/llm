from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file
import subprocess

# def main():
#     get_files_info("calculator", ".")
#     get_files_info("calculator", "pkg")
#     get_files_info("calculator", "/bin")
#     get_files_info("calculator", "../")

# main()

# def main():
#     #get_file_content("calculator", "lorem.txt")

#     get_file_content("calculator", "main.py")
#     get_file_content("calculator", "pkg/calculator.py")
#     get_file_content("calculator", "/bin/cat")
#     get_file_content("calculator", "pkg/does_not_exist.py")

# main()

# def main():
#     write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#     write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
#     write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

# main()

def main():
    run_python_file("calculator", "main.py")

main()

