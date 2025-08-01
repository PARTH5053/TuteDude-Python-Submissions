
# ----------- Task 2: Demonstrate List Slicing -------------

# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

nums = [i for i in range(1,11)] # Creates a list of numbers from 1 to 10.
print(nums)

first5Nums = nums[:5] # Extracts the first five elements from the list.
print(first5Nums)

rev_first5Nums = first5Nums[::-1] # Reverses these extracted elements.
print(rev_first5Nums)