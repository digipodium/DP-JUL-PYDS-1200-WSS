# return value
def area():
    l = int(input('enter the length:'))
    b = int(input('enter the breadth:'))
    return l * b

def minmax():
    x = [23,3,2,1,2,5,5,31]
    return min(x), max(x) # returning more than 1 value

# calling

# print("area=>", area())

# ans = area()
# print('area=>', ans)

# ans = area() + area() - area()
# print('total area=>', ans)

values = minmax()

x,y = minmax()

print(values)
print(x, y)
print(minmax())