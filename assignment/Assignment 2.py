#!/usr/bin/env python
# coding: utf-8

# Q1 
# What will the following code display?
# numbers = [1, 2, 3, 4, 5]
# print(numbers[1:-5])
# Can you debug and fix the output? The code should return the entire list

# In[1]:


# It didn't print anything. We can use the following command to print the entire list:
numbers = [1, 2, 3, 4, 5]
print(numbers[:])


# Q2
# Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

# In[2]:


# Create a list of days of the week
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Initialize an empty list to store sales data for each day of the week
weekly_store_sales = []

# Use a loop to collect sales data for each day
for day in days_of_the_week:
    sales = int(input(f"Please enter the store's sale on {day}: "))
    weekly_store_sales.append(sales)

# Calculate the total sales for the week
total_sales = sum(weekly_store_sales)

# Print the total store's sales
print("The total sale of the week is:", total_sales)


# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
# ● Print your list in its original order.
# ● Use the sort() function to arrange your list in order and reprint your list.
# ● Use the sort(reverse=True) and reprint your list.

# In[3]:


# Create list of places I would like to go
place_to_visit = ['Paris', 'Atlanta', 'London', 'Cancun', 'Miami']
# Print the list of places
print(place_to_visit)
# Sort the list of places
place_to_visit.sort()
print(place_to_visit)
# Use the reverse in the function sort
place_to_visit.sort(reverse=True)
print(place_to_visit)


# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.
# 

# In[4]:


# Create course dictionary
course_room_numbers = {'Data602':'Room1', 'Data605': 'Room2', 'Data606':'Room3'}
course_instructor_name = {'Data602':'Mike', 'Data605': 'Gavi', 'Data606':'Messi'}
course_meeting_time = {'Data602':'6:00pm', 'Data605': '7:00pm', 'Data606':'8:00pm'}

# List of courses
courses = ['Data602','Data605','Data606']
print(courses)

# Ask the user to enter the name of the course
user_course_number = input("Enter a course number: ")  

# Check if the courses entered is in the courses list 
if user_course_number in courses:
        print("Course Name: ", course_room_numbers[user_course_number] )
        print("Instructor: ", course_instructor_name[user_course_number] )
        print("Meeting Time: ", course_meeting_time[user_course_number] )
else:
        print("Course not found!")


# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.

# In[6]:


# Create a dictionary to store names and email addresses
address_book = {}

# Print options to the user
print("1. Look up an email address")
print("2. Add a new contact")
print("3. Change an email address")
print("4. Delete a contact")
    
    
# Ask the user to enter a choice    
choice = input("Enter your choice (1/2/3/4): ")
    
#  look up an email address   
if choice == '1':
    name = input("Enter the name to look up: ")
    if name in address_book:
        print(address_book[name])
    else:
        print("Name not found in the address book.")
        
# Add a new name and email address
elif choice == '2':
    name = input("Enter the new name: ")
    email = input("Enter the new email address: ")
    address_book[name] = email
    print(f"Added {name}'s email address: {email}")
        
# Change an existing email address       
elif choice == '3':
    name = input("Enter the name to change email address: ")
    new_email = input("Enter the new email address: ")
    if name in address_book:
        address_book[name] = new_email
        print(f"Updated {name}'s email address to: {new_email}")
    else:
        print("Name not found in the address book.")
        
# Delete an existing name and email address.      
elif choice == '4':
    name = input("Enter the name to delete: ")
    if name in address_book:
        del address_book[name]
        print(f"Deleted {name}'s contact information.")
    else:
        print("Name not found in the address book.")
        
        
else:
    print("Invalid choice. Please enter a valid option.")

