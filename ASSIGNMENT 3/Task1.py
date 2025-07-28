# ------------ Task 1: Calculate Factorial Using a Function -----------------------


# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.


# --- Using Recursion ---

# def factorial(num):
#     if num < 0:
#         return "Please enter valid number."
#     if num == 0 or num == 1:
#         return 1
#     return num * factorial(num-1)

# --- Using Function ---
def factorial(num):
    fact = 1
    if num < 0:
        return "Please enter valid number."
    if num == 0 or num == 1:
        return fact
    else:
        for i in range(2,num+1):
            fact = fact * i
        return fact

number = 5
print(f"Factorial of {number} is : {factorial(number)}")
