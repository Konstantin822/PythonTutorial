# name = input('Enter your full name: ')
# phone_number = input('Enter your phone #: ')

# result = len(name)  length of a string
# result = name.find('B') find the first occurence
# result = name.rfind('o') find the last occurrence, if no occurrence returns -1
# name = name.capitalize() capitalize the first character
# name = name.upper() UpperCase
# name = name.lower() LowerCase
# result = name.isdigit() return boolean, checks if there only numbers
# result = name.isalpha() return boolean, checks if there only alphabetical characters
# result = phone_number.count('-') count how many characters are within the string
# phone_number = phone_number.replace('-', ' ') replace characters

# print(help(str)) list of available string methods
 
username = input('Enter a username: ')


if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(' ') == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f'Welcome {username}')