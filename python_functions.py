# # Define a function named is_two. It should accept one input and return True if the 
# # passed input is either the number or the string 2, False otherwise.

# def is_two(value):
#     if value == '2' or value == 2:
#         return 'True'
#     else:
#         return 'False'
# print(is_two(2))

# # Define a function named is_vowel. It should return True if the passed string is a vowel, 
# # False otherwise.

# def is_vowel(letter):
#     if letter in ['a', 'e', 'i', 'o', 'u']:
#         return 'True'
#     else:
#         return 'False'

# def is_vowel(letter):
#         return letter in 'aeiou'

# print(is_vowel('a'))
# print(is_vowel('b'))

# print(is_vowel('a'))
# print(is_vowel('r'))

# # Define a function named is_consonant. It should return True if the passed string is a 
# # consonant, False otherwise.

# def is_consonant(letter):
#     if letter not in ['a','e','i','o','u']:
#         return 'True'
#     else:
#         return 'False'

# print(is_consonant('t'))
# print(is_consonant('a'))

# def is_consonant(letter):
#         return letter not in 'aeiou'

# print(is_consonant('a'))
# print(is_consonant('b'))

# # Define a function that accepts a string that is a word. The function should capitalize 
# # the first letter of the word if the word starts with a consonant.

# def is_consonant(letter):
#     if letter not in ['a','e','i','o','u']:
#         return str(letter.upper())
#     else:
#         return 'starts with a vowel'
    

# def cap_first_init(word):
#     if is_consonant(word[0]) == 'starts with a vowel':
#         return(word)
#     else:
#         return word.capitalize()

# print(cap_first_init('dog'))
# print(cap_first_init('eagle'))
# print(cap_first_init('bird'))
# print(cap_first_init('aardvark'))

# # Define a function named calculate_tip. It should accept a tip percentage (a number 
# # between 0 and 1) and the bill total, and return the amount to tip.
# # Calculates, but prints the {}s instead of values.

# def calculate_tip(pre_tip, tip_percentage):
#     return('The bill is ${}, and the tip is {}%.  The tip will be $'.format(pre_tip, tip_percentage))

# print(calculate_tip(5, .2))

# def tip(bill, tip_percent):
#     return bill * tip_percent

# # Define a function named apply_discount. It should accept a original price, and a discount 
# # percentage, and return the price after the discount is applied.

# def apply_discount(original_price, discount_percentage):
#     output = original_price - (original_price * discount_percentage)
#     return('The original price is ${}, it is {} off, the new total is ${}.'.format(original_price, discount_percentage, output))

# print(apply_discount(50, .1))

# # Define a function named handle_commas. It should accept a string that is a number 
# # that contains commas in it as input, and return a number as output.

# def handle_commas(number_string):
#     output = int(number_string.replace(',',''))
#     return output

# print(handle_commas('1,333,232,454'))
# print(type(handle_commas('1,333,232,454')))

# def handle_commas(number_string):
#     output = int(number_string.replace(',',''))
#     return('{} without commas is {}.'.format(number_string, output))

# print(handle_commas('1,333,232,454'))


# # Define a function named get_letter_grade. It should accept a number and return 
# # the letter grade associated with that number (A-F).

# def get_letter_grade(grade):
#     if grade >= 90:
#         output = 'A'
#     elif grade >= 80:
#         output = 'B'
#     elif grade >= 70:
#         output = 'C'
#     elif grade >= 60:
#         output = 'D'
#     else:
#         output = 'F'
#     return('Your grade of {} has earned you a {}.'.format(grade, output))

# print(get_letter_grade(88))
# print(get_letter_grade(75))
# print(get_letter_grade(94))

# Define a function named remove_vowels that accepts a string and returns a string 
# with all the vowels removed.

# # def remove_vowels(word):
# #     vowel in ['a','e','i','o','u']

# def isVowel(words):
#         new_word = words.lower()
#         vowels = ('a','e','i','o','u')
#         for letter in words:
#                 if letter in vowels:
#                         new_word = new_word.replace(letter,'')
#         return new_word
# print(isVowel('dog'))
# print(isVowel('Aardvark\'s are my favorite animal.'))
# print(isVowel('AaBbEeRr'))

# # Define a function named normalize_name. It should accept a string and return 
# # a valid python identifier, that is:
# # -anything that is not a valid python identifier should be removed
# # -leading and trailing whitespace should be removed
# # -everything should be lowercase
# # -spaces should be replaced with underscores
# # -for example:
# #       -Name will become name
# #       -First Name will become first_name
# #       -% Completed will become completed

# IDENTIFIERS = 'abcdefghijklmnopqrstuvwxyz123456789_0'

# def normalize_name(a_string):
#         a_string = a_string.strip().replace(' ','_').lower()
#         valid_characters = []
#         for character in a_string:
#                 if character in IDENTIFIERS:
#                         valid_characters.append(character)
#         return ''.join(valid_characters)

# print(normalize_name('  as #$% 45 ADG 4%4   '))

# def removes_leading_trailing_whitespace(user_input):
#         user_input_whitespace_removed = user_input.strip()
#         return user_input_whitespace_removed

# def replaces_inner_white_space_with_underscore_leading_trailing_already_removed(user_input):
#         user_input_no_whitespace = removes_leading_trailing_whitespace(user_input).replace(' ','_')
#         return user_input_no_whitespace

# # # # Only removes first non identifier, need to tweek:

# def no_white_space_remove_non_valid_identifiers_and_lowercase(user_input):
#         string_to_remove_identifiers_from = replaces_inner_white_space_with_underscore_leading_trailing_already_removed(user_input).lower()
#         valid_identifiers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','_','0']
#         final_word = []
#         for char in string_to_remove_identifiers_from:
#                 if char in valid_identifiers:
#                         final_word.append(char)
#         return ''.join(char)
# print(no_white_space_remove_non_valid_identifiers_and_lowercase('  abd  ase $da AD   '))
# print(no_white_space_remove_non_valid_identifiers_and_lowercase('  aw34 42$@$42 JKHN lkn   ,.4  r   '))
# print(no_white_space_remove_non_valid_identifiers_and_lowercase('  asei &;l  45 , asd  AD  d   '))
# print(no_white_space_remove_non_valid_identifiers_and_lowercase('  #a 4 $ , ^ & # @ * ! 4 >> r'))


# def no_white_space_remove_non_valid_identifiers_and_lowercase(user_input):
#         string_to_remove_identifiers_from = replaces_inner_white_space_with_underscore_leading_trailing_already_removed(user_input).lower()
#         valid_identifiers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','_','0']
#         for char in string_to_remove_identifiers_from:
#                 if char not in valid_identifiers:
#                         no_white_space_and_non_identifiers_removed_and_all_lowercase = string_to_remove_identifiers_from.replace(char,'')
#                         return no_white_space_and_non_identifiers_removed_and_all_lowercase
# print(no_white_space_remove_non_valid_identifiers_and_lowercase('  abd  ase $da AD   '))
# print(no_white_space_remove_non_valid_identifiers_and_lowercase('  aw34 42$@$42 JKHN lkn   ,.4  r   '))
# print(no_white_space_remove_non_valid_identifiers_and_lowercase('  asei &;l  45 , asd  AD  d   '))
# print(no_white_space_remove_non_valid_identifiers_and_lowercase('  #a 4 $ , ^ & # @ * ! 4 >> r'))

# Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# def cumsum(numbers):
#         sums = [numbers[0]]
#         for current_number in numbers[1:]:
#                 last_number = sums[-1]
#                 next_number = last_number + current_number
#                 sums.append(next_number)
#         return sums

# print(cumsum([1,2,3]))
# print(cumsum([2,4,6,5]))

# Needs tweeking. 1, 2, 4 shows as multiple arguments entered.
# def verifies_list(user_input):
#         type_list_verified = user_input
#         if type(user_input) == list:
#                 return type_list_verified
#         else:
#                 return('This is not a list.')

# print(verifies_list([1,3,5]))
# print(verifies_list([1,3,4,5,5]))

# def list_contains_numbers(user_input):
#         list_of_numbers = user_input.split()
#         # if type(list_of_numbers) == int:
#         #         return list_of_numbers.join()
#         # else:
#         #         return('These are not numbers.')

# print(list_contains_numbers([1,2,3]))

# example = [1,2,3]
# import numpy as np
# summed_example = np.cumsum(example)
# print(summed_example)
