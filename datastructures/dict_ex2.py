movies = {
    'm1':'Sholay',
    'm2': 'Spiderman: No way home',
    'm3': 'Shrek'
}

print(movies)
print(movies.keys())
print(movies.values())

# traversing a dictionary -> style 1 -> gives only keys
print('style 1')
for name in movies:
    print(name)

# traversing a dictionary -> style 2 -> gives only values
print('style 2')
for key in movies:
    print(movies[key])

# traversing a dictionary -> style 3 -> gives keys and values
print('style 3')
for key in movies:
    print(key, movies[key])

# traversing a dictionary -> style 4 -> gives keys and values
print('style 4')
for k, v in movies.items():
    print(k, v)
