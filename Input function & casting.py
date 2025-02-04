# Q1: Write a Python program to input student name and marks of subjects.
# Print name & percentage in output.

student_name = input("Enter the student name: ")
math_marks = int(input("Enter math marks: "))
hindi_marks = int(input("Enter hindi marks: "))
eng_marks = int(input("Enter eng marks: "))
sci_marks = int(input("Enter sci marks: "))

# Calculate percentage % of marks:

percentage = ((math_marks + hindi_marks + eng_marks + sci_marks)/400)*100

print(f"student name is {student_name}.")
print(f"math marks is {math_marks}.")
print(f"english marks is {eng_marks}.")
print(f"science marks is {sci_marks}.")
# I will Round function. because, want just one digit after decimal.
print(f"And, Last percentage % is {round(percentage,1)}")

# Q2: Write a Python programe that collects multiple types of data
# (e.g., name, age, height, and student status) from user input, stores
# them in dictinary, and then prints out the collected data?

# intializing the dictionary

user_data = {}

# input from users

user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['Status'] = input("Enter student status active/non-active: ")

# print the input from user

print(user_data)

