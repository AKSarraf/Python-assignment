# 1: Limit the decimal places to 2 digits using format method to and
# print result, for the variable pi = 3.14159265359.

# pi = 3.14159265359

# print("value of pi is {:.2f}".format(pi))
 

# 2: Extract characters from index 2 to 8 with step of 2 given my_string 
# = "Python Course", slice character from index 2 to 8, skipping evrey other
# char.

# my_string = "python Course"

# # string[start:stop:step]
# print(my_string[2:8:2])

# 3: Slice to get only the middle character(s). for my_string = "Madhav",
# using slicing to extract the middle character(s).

# my_string = "ankit"
# my_string1 = "ankita"

# def mid_str(word):
#     middle = int(len(word)/2)
#     if len(word) % 2 == 0:
#         return word[middle-1:middle+1]
#     else:
#         return word[middle]
# print(mid_str(my_string))
# print(mid_str(my_string1))

# 4: Remove the first 3 and last 3 character: given my_string =
# "Regression Analysis", remove the first 3 and last 3 characters.

# my_string = "Regression Analysis"

# print(my_string[3:-3])

# 5: Get the substrings that starts 4 characters from the end to the last
# character: for my_sting = "Classification", slice the string starting
# from 4th character from the end to the last character.

# my_string = "Classification"

# print(my_string[-4:])

# 6: How to Resverse a string using Python String Methods?


# my_string = "Classification"

# print(my_string[::-1])    # step value is -1.

# 7: Write Python function to check if a string is a palindrome using 
# strind methods.

word = "madam"

def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a plindrome")
    else:
        print(f"{s} is not a plindrome")

print(is_palindrome(word))