
def word_counter(s):
    words =s.split()
    return len(words)

def area(l,b):
    return l * b

def circmuference(r):
    return 2 * 3.14 * r

print(word_counter('This is an example'))
print(word_counter('Welcome to the code of python'))
print(word_counter("screenshot se kuch nhi hota"))
print(word_counter('rules and covention likh lo!!!'))

# CALL area and circumference

# 1. direct 
print(area(10,10))

# 2. user input
a = int(input('enter length: '))
b = int(input('enter breadth: '))
out = area(a, b)
print('area=>>', out)

# 3. shorter user input
out = area(int(input('lenght:')), int(input('breadth:')))
print('area=>', out)