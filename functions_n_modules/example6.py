x = [2,2,3,1,2,3,5,6,2,2,1]

x5 = list(map(lambda i: i-5, x))
print(x5)

y = [2,3,1,2,3,5,6,3,3,1,2]

xy = list(map(lambda a,b: a + b, x, y))
print(xy)

y3 = list(filter(lambda i: i>3, x))
print(y3)

name = ['Raj Singh','Vijay Singh','Ravi Kumar',
        'Ajay Singh','Raja Kumar','Vijay Pandey']

name_singh = list(filter(lambda n: n.endswith('Singh'), name))
print(name_singh)

