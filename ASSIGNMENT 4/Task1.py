# ---------- Task 1: Read a File and Handle Errors ------------

# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.


file_path = "sample.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print("Reading File content:")
        print(content)

except FileNotFoundError:
    print(f'ERROR! The File {file_path} Not Found!')

except Exception as e:
    print(f"An error occurred: {e}")

