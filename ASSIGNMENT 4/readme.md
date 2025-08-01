Task 1: Read a File and Handle Errors
Goal:
Read the content of a file named sample.txt and handle any errors that may occur if the file is missing or unreadable.

What it does:
Tries to open sample.txt and read its content.

Prints the content line by line.

If the file doesn't exist, it gracefully shows an error message instead of crashing the program.

Output:

Reading File content:

This is a sample file.

It contains multiple lines.

Error Handling:

If sample.txt is not found:

ERROR! The File sample.txt Not Found!




Task 2: Write and Append Data to a File

Goal:
Take user input, write it to a file (output.txt), then append more input, and finally read and display the final file content.


What it does:
Asks the user to input some text and writes it to output.txt.


Then, it takes more input and appends it to the same file.


Finally, it reads and prints the complete content of output.txt.


Example Output:

Enter text to write to the file: Hello

Enter additional text to append: World

Final content of output.txt : 

Hello

World

Error Handling:

If anything goes wrong while accessing the file, it will show a friendly error message without crashing.


