# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
first_name = 'User'
food = 'pizza'
email = 'test@fake.com'

print(f'Hello {first_name}') # begin a string with f or F to use Python expression between {}
print(f'You like {food}')
print(f'Your email is {email}')

# Integers
age = 28
quantity = 3
num_of_students = 30

print(f'You are {age} years old')
print(f'You are buing {quantity} items')
print(f'Your class has {num_of_students}')

# Float
price = 10.99
gpa = 3.2
distance = 5.5

print(f'The price is ${price}')
print(f'Your gpa is {gpa}')
print(f'You ran {distance}km')

# Boolean
is_student = True
for_sale = True
is_online = False

if is_student:
    print('You are a student')
else:
    print('You are not a student')    

print(f'Are you a student?: {is_student}')

if for_sale:
    print('That item is for sale')
else:
    print('That item is NOT available')

if is_online:
    print('You are online')
else:
    print('You are offline')

# Task
user_name = 'Bariy'
year = 2026
pi = 3.14
is_admin = True

if is_admin:
    print('You are admin')
else:
    print('You are NOT admin')    

print(f'Your user name is {user_name}')