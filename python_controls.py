# 1. Conditional Basics
# Prompt the user for a day of the week, print out whether the day is Monday or not.
# I need to change to a while loop and make sure an invalid entry prompts user for another entry.

# day_of_the_week = input('Please enter a day of the week: ')
# not_monday = ['Sunday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# if day_of_the_week == 'Monday':
#     print('Why did you just pick Monday?')
# elif day_of_the_week in not_monday:
#     print('Oh, so you\'re a fan of '+day_of_the_week+'.')
# else:
#     print('I asked about your favorite day.')

# Prompt the user for a day of the week, print out whether the day is a weekday or a weekend.

# day_of_the_week2 = input('Please enter a day of the week: ')
# if day_of_the_week2 == 'Saturday' or day_of_the_week2 == 'Sunday':
#     print('Weekends are awesome!')
# elif day_of_the_week2 == 'Monday' or day_of_the_week2 == 'Tuesday' or day_of_the_week2 == 'Wednesday' or day_of_the_week2 == 'Thursday' or day_of_the_week2 == 'Friday':
#     print('I guess weekdays are alright.')
# else:
#     print('Did you enter a day?')

# Create variables and make up values for the number of hours worked in one week,
# the hourly rate, how much the week's paycheck will be.
# Write a python code that calculates the weekly paycheck, overtime is time and a half after 40 hours.

# hours_worked_this_week = float(input('How many hours did you work this week? '))
# hourly_rate = float(input('How much do you make per hour? '))
# if hours_worked_this_week > 40:
#     base_pay = 40 * hourly_rate
#     overtime_pay = (hours_worked_this_week - 40) * (hourly_rate * 1.5)
#     pay_check = base_pay + overtime_pay
# else:
#     pay_check = hours_worked_this_week * hourly_rate

# print('This week, you worked '+str(hours_worked_this_week)+' hours.  With overtime, you can expect your paycheck to be $'+str(pay_check)+'.')

# 2. Loop Basics
# Increment an integer value from 5 to 15.
# i = 5
# while i <= 15:
#     print(i)
#     i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# i = 0
# while i <= 100:
#     print(i)
#     i += 2

# This next solution does not include zero, but practices continue:

# i = 0
# while i < 101:
#     i += 1
#     if i % 2 != 0:
#         continue
#     print(i)

# Alter your loop to count backwards by 5's from 100 to -10.

# i = 100
# while i >= -10:
#     print(i)
#     i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while
# the number is less than 1,000,000.

# i = 2
# while i <= 1_000_000:
#     print(i)
#     i = i ** 2

# Write a loop that starts at 100 and reduces by 5, but does not include 0.

# i = 100
# while i >= 5:
#     print(i)
#     i -= 5

# # or

# for n in range(100, 0, -5):
#     print(n)

# Write some code that prompts the user for a number, then shows a multiplication table up through 10
# for that number.

# your_number_multiplied_to_ten = input('Please enter a positive integer: ')
# if (your_number_multiplied_to_ten.isdigit() == True) and (int(your_number_multiplied_to_ten) > 0):
#     multiplied_by = 1
#     while multiplied_by <= 10:
#         print(str(your_number_multiplied_to_ten)+' x '+str(multiplied_by)+' = '+str(int(your_number_multiplied_to_ten)*multiplied_by))
#         multiplied_by +=1

# # or

# your_number_multiplied_to_ten = input('Please enter a positive integer: ')
# while not your_number_multiplied_to_ten.isdigit() or (int(your_number_multiplied_to_ten) < 0):
#     your_number_multiplied_to_ten = input('Remember to make it a positive integer: ')
# else:
#     for multiplied_by in range(1, 11):
#         output = '{} x {} = {}'.format(your_number_multiplied_to_ten, multiplied_by, your_number_multiplied_to_ten * multiplied_by)
#         print(output)
        

# Create a loop that outputs one 1, two 2's, etc. ending with nine 9's.

# number = 1
# while number <= 9:
#     print(str(number)*number)
#     number += 1

# for number in range(1,10):
#     print(str(number)* number)
#     number += 1

# Create a loop that will ask a user to input an odd number between 1 and 50.  The output will show
# all odd numbers from 1-50 and will include a line stating that the user's number is being skipped.
# If the user does not input an odd number between 1 and 50, prompt them for another entry.

# your_odd_number_skipped = input('Please enter an odd number between 1 and 50: ')
# while not your_odd_number_skipped.isdigit() or (int(your_odd_number_skipped) % 2 == 0) or (int(your_odd_number_skipped) <= 0) or (int(your_odd_number_skipped) >= 51):
#     your_odd_number_skipped = input('Please enter another number that is odd and between 1 and 50: ')
# else:
#     print('Number to skip is: '+ your_odd_number_skipped)
#     for odd_number in range(1, 51):
#         if odd_number == int(your_odd_number_skipped):
#             print('Yikes!  Skipping number: '+your_odd_number_skipped)
#         elif odd_number != int(your_odd_number_skipped) and odd_number % 2 != 0:
#             print('Here is an odd number: '+str(odd_number))

# Prompt the user to enter a positive number and write a loop that counts from 0 to that number.

# zero_to_your_number = input('Please enter a positive integer: ')
# while (zero_to_your_number.isdigit() == False) or (int(zero_to_your_number) <= 0):
#     zero_to_your_number = input('I said a positive integer, please: ')
# else:
#     for pi in range(0, int(zero_to_your_number)+1):
#         print(pi)

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the
# numbers from the number the user entered down to 1.

# positive_integer_counted_down_to_one = input('Please enter a positive integer: ')
# while not positive_integer_counted_down_to_one.isdigit() or int(positive_integer_counted_down_to_one) <= 0:
#     positive_integer_counted_down_to_one = input('Please change that to a positive integer: ')
# else:
#     for integer in range (int(positive_integer_counted_down_to_one), -1, -1):
#         print(integer)
#         integer -= 1
#         if integer <= -1:
#             break

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz"
# For numbers which are multiples of both three and five print "FizzBuzz".

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print('FizzBuzz')
#     elif number % 5 == 0:
#         print('Buzz')
#     elif number % 3 == 0:
#         print('Fizz')
#     else:
#         print(number)

# Display a table of powers:
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

# factored_number_input = input('Please enter a positive integer: ')
# while factored_number_input.isdigit() == False or int(factored_number_input) <= 1:
#     factored_number_input = input('Please adjust your answer to a positive integer: ')
# else:
#     for number in range(1, int(factored_number_input)+1):
#         print(number, number ** 2, number ** 3)
#         number += 1
#         if number > int(factored_number_input):
#             break

# # Goback and work on the one below, trying to work with formatting...
# factored_number_input = input('Please enter a positive integer: ')
# while factored_number_input.isdigit() == False or int(factored_number_input) <= 1:
#     factored_number_input = input('Please adjust your answer to a positive integer: ')
# else:
#     for number in range(1, int(factored_number_input)+1):
#         print('number | squared | cubed')
#         print('{} | {} | {}'.format(number, number ** 2, number ** 3)
#         number += 1
#         if number > int(factored_number_input):
#             break
# want_to_continue = input('Would you like to continue: ')
# if want_to_continue == 'Yes' or want_to_continue == 'Y':
#     print('Let\'s continue...')

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# submitted_grade = input('Please enter a grade from 0 to 100: ')
# while submitted_grade.isdigit() == False or int(submitted_grade) < 0 or int(submitted_grade) > 100:
#     submitted_grade = input('Please change your answer to an integer between 0 and 100: ')
# if 100 >= int(submitted_grade) >= 88:
#     print('Hot diggity dog.  Your score of '+submitted_grade+' earned you an A.')
# elif 87 >= int(submitted_grade) >= 80:
#     print('Way to go, champ!  Your '+submitted_grade+' is a solid B.')
# elif 79 >= int(submitted_grade) >= 67:
#     print('Alright, a C.')
# elif 66 >= int(submitted_grade) >= 60:
#     print('Hey, you got a D.')
# else:
#     print('Let\'s work to raise that grade.')
# want_to_continue = input('Would you like to continue: ')
# if want_to_continue == 'Yes' or want_to_continue == 'Y':

# submitted_grade = input('Please enter a grade from 0 to 100: ')
# while submitted_grade.isdigit() == False or int(submitted_grade) < 0 or int(submitted_grade) > 100:
#     submitted_grade = input('Please change your answer to an integer between 0 and 100: ')
# if 100 >= int(submitted_grade) >= 88:
#     print('Hot diggity dog.  Your score of '+submitted_grade+' earned you an A.')
# elif 87 >= int(submitted_grade) >= 80:
#     print('Way to go, champ!  Your '+submitted_grade+' is a solid B.')
# elif 79 >= int(submitted_grade) >= 67:
#     print('Alright, a C.')
# elif 66 >= int(submitted_grade) >= 60:
#     print('Hey, you got a D.')
# elif int(submitted_grade) < 60:
#     print('Let\'s work to raise that grade.')
# want_to_continue = input('Would you like to continue: ')
# # Can I += the variable to keep it going?
# submitted_grade = input('Please enter a grade from 0 to 100: ')
# while (submitted_grade.isdigit() == False) or (int(submitted_grade) < 0) or (int(submitted_grade) > 100):
#     submitted_grade = input('Please change your answer to an integer between 0 and 100: ')
# if 100 >= int(submitted_grade) >= 88:
#     print('Hot diggity dog.  Your score of '+submitted_grade+' earned you an A.')
# elif 87 >= int(submitted_grade) >= 80:
#     print('Way to go, champ!  Your '+submitted_grade+' is a solid B.')
# elif 79 >= int(submitted_grade) >= 67:
#     print('Alright, a C.')
# elif 66 >= int(submitted_grade) >= 60:
#     print('Hey, you got a D.')
# elif int(submitted_grade) < 60:
#     print('Let\'s work to raise that grade.')

# Create a list of dictionaries where each dictionary represents a book that you have read.
# Each dictionary in the list should have the keys title, author, and genre. Loop through the list
# and print out information about each book.
# Prompt the user to enter a genre, then loop through your books list and print out the
# titles of all the books in that genre.

# read_books = [
#     {'Title': 'The DaVinci Code', 
#     'Author': 'Dan Brown', 
#     'Genre': 'Suspense'},

#     {'Title': 'The Five People You Meet in Heaven',
#     'Author': 'Mitch Albom', 
#     'Genre': 'Inspirational'},

#     {'Title': 'Calvin and Hobbes One Day the Wind Will Change',
#     'Author': 'Bill Watterson', 
#     'Genre': 'Comedy'},

#     {'Title': 'Test',
#     'Author': 'Test McTesterson', 
#     'Genre': 'Comedy'}
# ]
# genre_of_book_you_chose = input(
#     'Choose between Suspense, Inspirational, or Comedy: ')
# while not genre_of_book_you_chose in ['Suspense', 'Inspirational', 'Comedy']:
#     genre_of_book_you_chose = input(
#         'Your choices are Suspense, Inspirational, or Comedy: ')
# for book in read_books:
#     if book['Genre'] == genre_of_book_you_chose:
#         print(book['Title'])

# #Trying to create a loop so that the options in the input question will be updated 
# # if another genre is added.
# read_books = [
#     {'Title': 'The DaVinci Code', 
#     'Author': 'Dan Brown', 
#     'Genre': 'Suspense'},

#     {'Title': 'The Five People You Meet in Heaven',
#     'Author': 'Mitch Albom', 
#     'Genre': 'Inspirational'},

#     {'Title': 'Calvin and Hobbes One Day the Wind Will Change',
#     'Author': 'Bill Watterson', 
#     'Genre': 'Comedy'},

#     {'Title': 'Test',
#     'Author': 'Test McTesterson', 
#     'Genre': 'Comedy'}
# ]

# for book in read_books:
#     genre_of_book_you_chose = input('Choose between ' + 
#     str(book['Genre'] in 'Genre')
#     + ': ')
#     if genre_of_book_you_chose not in book['Genre']:
#         continue
#     if book['Genre'] == genre_of_book_you_chose:
#         print(book['Title'])