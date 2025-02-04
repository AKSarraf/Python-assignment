# Q1: Leap Year: Write a simple program to determine if a given year
# is a leap year using user input.
 
# Note:

# Leap year occurs once every four years.
# A year is a leap year if it is divisible by 4, but not if it is
# divisible by 100 unless it is also divisible by 400.

# create leap_year function.

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

# # Taking user input

year = int(input("Enter the year: "))


# checking for leap_year

if leap_year(year):
    print(f"It is a leap {year}")
else:
    print(f"It is not leap_year {year}")

# Q2: Login Authentication using conditional statement. Assume you have a
# predefined username and password.

# Write a program that prompts the user to enter username and password
# and checks whether they match. Provide appropriate messages for the
# Following cases:

# Both username and password are correct.
# Username is correct but password is incorrect.
# Username is incorrect.

# predefined username and password.
predefined_username = "Ankitsoni9560@gmail.com"
predefined_password = "@Nkit83839891"

# # Prompts the user to enter a surname and password:

username = input("Enter your username: ")
password = input("Enter your Password: ")

# # username and password match.

if predefined_username == username:
    if predefined_password == password:
        print("Welcome in login")
    else:
        print("incorrect Password")
else:
    print("incorrect username")

# Q3: Admission Eligibility: A Unversity has the following
# eligibilty criteria for admission:

    # marks in mathematics >= 65
    # marks in physics >= 55
    # marks in chemsistry >= 50
    # Total marks in all three subjects >= 180 OR Total marks
    # Mathematics and physics >= 140

# Write a program that takes marks in three subjects as input and
# prints whether the student is eligible for admission.

# user input

print("Enter PCM marks out of 100")
math_marks = int(input("Enter the marks: "))
phy_marks = int(input("Enter the marks: "))
chem_marks = int(input("Enter the marks: "))

# Check eligiblity criteria of student:

if (math_marks >= 65 and
    phy_marks >= 55 and
    chem_marks >= 50 and
    (math_marks + phy_marks + chem_marks) >= 180) or \
    (math_marks + phy_marks) >= 140:
    print("Student is eligible")
else:
    print("Student are not eligible")



