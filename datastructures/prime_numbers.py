# create a prime number list upto size n
# 2, 3, 5, 7, 11, 
primes = []
for num in range(2, 10000):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        primes.append(num)

for p in primes:
    print(p, end=', ')