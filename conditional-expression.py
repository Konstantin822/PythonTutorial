# conditional expression = A one-liner shortcut for the if-else statement (ternary operator)
#                          Print or assign one of thwo values based on a condition
#                          X if condition else Y

num = 5
a = 6
b = 7
age = 17
temperature = 20
user_role = 'admi'

# print('Positive' if num > 0 else 'Negative')
# result = 'EVEN' if num % 2 == 0 else 'ODD'
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = 'Adult' if age >= 18 else 'Child'
# weather = 'HOT' if temperature > 20 else 'COLD'
access_level = 'Full Access' if user_role == 'admin' else 'Limited Access'

print(access_level)