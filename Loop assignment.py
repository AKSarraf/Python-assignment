# Q1: Print in the same line.
# i = 1
# while i < 4:
#     print(f"hello ankit {i}", end = " ")
#     i += 1

# Q2: Prints star pattern in loop.

# n = 5 # num of rows

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()


# Q3: print Inverted triangle.

# n = 5

# for i in range(n, 0, -1):
#     print("* " * i)

# # Q3: pyramid pattern triange

# n = 5

# for i in range(1, n+1):
#     print(" " * (n-i), end = "")
#     print("*" * (2 * i - 1))


# Q5: Factorial by using loop:

# def factorial(n):
#     result =  1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result
# print(factorial(5))
 

# my_string = "Python by ankita kumari"

# vowels = "aioue"

# count = 0

# for char in my_string:
#     if char in vowels:
#         count += 1
# print("Number of vowels are", count)


# # Q7: Longest word in a string.

# Sentence = input("Enter the str: ")

# if not Sentence:
#     print("No input provided. please enter a sentence.")
# else:

#     words = Sentence.split()

#     longest_word = ""

#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word

#     print("The longest word is", longest_word)


# # Q8: Do-while loop in python.

# while True:
#     num = int(input("Enter a number greater than 10: "))

#     if num > 10:
#         print(f"Valid number entered: {num}")
#         break # exit the loop when condition is satisfied
#     else:
#         print("Number is not greater than 10, try again!")


# Q9: fibonacci sequence.

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a)
        a,b = b,a+b
        count += 1
fibonacci(10)


