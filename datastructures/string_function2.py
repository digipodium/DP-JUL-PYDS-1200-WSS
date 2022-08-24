# string validation function
value = input('enter something:')

# test
if value.isnumeric():
    print("Only Numbers", value.isnumeric())
if value.isalpha():
    print('Only Alphabets', value.isalpha())
if value.isalnum():
    print('Alphabets & Numbers', value.isalnum())
if value.isspace():
    print('Only spaces', value.isspace())
if value.isupper():
    print('Uppercase Alphabets', value.isupper())
if value.islower():
    print('Lowercase Alphabets', value.islower())
