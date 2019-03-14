import functions_exercises as f
from functions_exercises import is_two as it
print(it(3))


from functions_exercises import is_vowel

print(itertools.accumlate([1,2,3]))

# # How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

import itertools as it
letters = 'ABC'
numbers = '123'
print(list(it.product(letters, numbers)))
print(len(list(it.product(letters, numbers))))

# # How many different ways can you combine two of the letters from "abcd"?

import itertools as it
letters = 'ABCD'
print(list(it.combinations(letters, 2)))
print(len(list(it.combinations(letters, 2))))

import json
import statistics

data = json.load(open('profiles.json'))


# Total number of users:

print(len(json.load(open('profiles.json'))))

Number of active users:

active = [user['isActive'] for user in data]
print(active)

active = [user['isActive'] for user in data]
print(active)

# Prints user id's that are currently active:
for user in data:
    if user['isActive'] == True:
        print(user['_id'])

# Trying to create the same active user id list by appending to a created list and producing a list.
for user in data:
    active_user_ids = []
    if user['isActive'] == False:
        continue
    else:
        active_user_ids.append(user['_id'])
print(active_user_ids)

# Trying a function:
def is_active(user):
    for user in data:
        active_user_ids = []
        if user['isActive'] == False:
            continue
        else:
            active_user_ids.append(user['_id'])
        return active_user_ids
            
print(is_active(data))


# Number of inactive users

inactive_users = []

for active in data:
    if active['isActive'] == False:
        inactive_users.append(row['isActive'])

print(len(inactive_users))

# Prints id's for non active users:
for user in data:
    if user['isActive'] == False:
        print(user['_id'])

# Creates list with all balances:

new_balance = []

for row in data:
    new_balance.append(row['balance'])

no_dollar_or_comma_balance =[]

for balance in new_balance:
    no_dollar_comma = balance[1:].replace(',','')
    no_dollar_or_comma_balance.append(no_dollar_comma)



print([float(i) for i in no_dollar_or_comma_balance])

print(min(no_dollar_or_comma_balance))
print(max(no_dollar_or_comma_balance))

# User with min balance
for user in data:
    if user['balance'] == '$1,214.10':
        print(user['name'])


print(new_balance)
print(type(new_balance))
print(type(new_balance[0]))

# Runs through list of balances and sums them

float_balances = 0.0

for user in new_balance:
    float_balances += float(user[1:].replace(',',''))

print(float_balances)

average_balance = float_balances / len(new_balance)

print(average_balance)





# for character in new_balance:
#     to_remove = '$.%'
#     useable_balance_string = []
#     if character in to_remove:
#         useable_balance_string.replace(to_remove,'')
#         print(useable_balance_string)
# print(useable_balance_string)
    


# def fl_balance(new_balance):
#     useable_balance_string = []
#     for sign in '$.':
#         useable_balance_string = useable_balance_string.replace(sign,'')
#     return useable_balance_string

# print(fl_balance(new_balance))
    



# for balance in data:
#     balance = (balance['balance'])

# no_comma = balance.replace(',','')
# useable = no_comma.replace('$','')
# useable = float(useable)
# print(useable)



# numbers = '123456789.0'


# def normalize_balance(balances):
#     new_balance = []
#     for balance in data:
#         return balance['balance']
#         if number in numbers:
#             new_balance.append(number)
#         return int(new_balance)

# print(normalize_balance(data))
        

# numbers = '123456789.0'

# def new_balance(data):
#     return data[['balance']]
#     new_balance = []
#     for number in data:
#         if number not in numbers:
#             continue
#         else:
#             new_balance.append(number)
#         return int(new_balance)

# print(new_balance(data))


