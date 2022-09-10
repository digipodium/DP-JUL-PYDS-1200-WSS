# create a list of n numeric elements
# - generate a list of only even number from existing list
# - generate a list of only odd number from existing list
# - generate a list of only number > n from existing list, where n can be any value

x = [2,4,5,1,4,6,7,8,9,4,2,5,6,22]

xe = []
for i in x:
    if i % 2 == 0:
        xe.append(i)

xo = []
for i in x:
    if i % 2 != 0:
        xo.append(i)


xg5 = []
for i in x:
    if i > 5:
        xg5.append(i)

n = int(input('enter a number'))
xgn = []
for i in x:
    if i > n:
        xgn.append(i)

print(x)
print(xe)
print(xo)
print(xg5)
print(xgn)

