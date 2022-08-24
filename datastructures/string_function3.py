# string validation

value =input("Enter the Guest name:")

if value.startswith('Mr.'):
    print("Welcome Sir")
elif value.startswith("Ms."):
    print("Welcome Ma'am")
elif value.startswith("Dr."):
    print("Welcome Doctor")
else:
    print('You are not invited')

    