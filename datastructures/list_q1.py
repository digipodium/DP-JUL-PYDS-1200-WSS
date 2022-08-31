# create a list will 10 values entered by user and the sort the values

x = []
for i in range(10):
    val = input(f'enter value {i+1}: ')
    x.append(val)

print("the list")
x.sort()
for val in x:
    print(val, end=' ')
# print(' '.join(x))