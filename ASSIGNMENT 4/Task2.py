# --------------- Task 2: Write and Append Data to a File -------------

# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

file_name = "output.txt"
try:
    text1 = input("Enter text to write to the file: ")
    with open(file_name, "w") as file:
        file.write(text1 + "\n")

    text2 = input("Enter additional text to append: ")
    with open(file_name, "a") as file:
        file.write(text2 + "\n")

    print("Final content of output.txt : ")
    with open(file_name,'r') as file:
        content = file.read()
        print(content)

except IOError as e:
    print(f"Error: {e}")