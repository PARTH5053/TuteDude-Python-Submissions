#  ----------------- Task 1: Create a Dictionary of Student Marks ---------------

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.


#Creates a dictionary where student names are keys and their marks are values.
student_dict = {
    "Parth" : 97,
    "Dhruvit" : 57,
    "Jay" : 78,
    "Krunal" : 80
}

# Asks the user to input a student's name
stu_name = input("Enter the Student's name : ")

if stu_name in student_dict:
    print(f"{stu_name}'s Marks : {student_dict[stu_name]}") # Retrieves and displays the corresponding marks
else:
    print(f"{stu_name} not found.") # If the student’s name is not found, display an appropriate message.