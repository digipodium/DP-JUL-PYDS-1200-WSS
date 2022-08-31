# create a list with 10 numeric values from user
# then find the min, max, total, avg, median

import statistics as stat

a = []
for i in range(1,11):
    val = int(input(f'enter number {i} ->'))
    a.append(val)

for i in a:
    print(i, end=' ')

print("minimum value: ", min(a))
print("maximum value: ", max(a))
print("total of values: ", sum(a))
print("average of values: ", stat.mean(a))
print('mediam of values:', stat.median(a))


