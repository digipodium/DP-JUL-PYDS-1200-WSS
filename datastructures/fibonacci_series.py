# create a fibbonacci series in a list of size n
# [0 1 1 2 3 5 8 13 26 ...]

fib = [0, 1,]
for i in range(100):
    fib.append(fib[-1] + fib[-2])
print(fib)