"""Kossi Akplaka
    Assignment 1
    Data 602
"""


#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
# Add the variable test 3 and convert the test scores to integers
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))
# Calculate the average test score.
# I corrected the calculation of the average
average = (test1 + test2 + test3) / 3
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
#I changed 'high_score' to 'HIGH_SCORE' to match the constant.
if average >= HIGH_SCORE:
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
# Get the width and the length of the first rectangle
length1 = float(input("Please enter the length of the rectangle 1: "))
width1 = float(input("Please enter the width of the rectangle 1: "))
# Get the width and the length of the second rectangle
length2 = float(input("Please enter the length of the rectangle 2: "))
width2 = float(input("Please enter the width of the rectangle 2: "))
# Find the area of both rectangles
area1 = length1 * width1
area2 = length2 * width2
# Print the area of both rectangles
print("the area of the rectangle 1 is:", area1)
print("the area of the rectangle 2 is:", area2)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int. 

#  Ask for the first name
name = input("Please enter your first name: ")
# Ask for the age
age = int(input("Please enter your age: "))

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

# Print birthday wishes
print(f"Happy birthday, {name}! You are {age} years old today!")
