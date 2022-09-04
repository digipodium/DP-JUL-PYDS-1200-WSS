from pprint import pprint

movies = {}

# adding a single value
movies['sholay'] = '2 frds fight with a dacoit'
movies['inception'] = 'no summary avaialable'

# adding multiple values
movies.update(
    ironman='man builds a suit that is not iron',
    hulk = 'story about a man that is not hulka',
    batman ='hero dressed as a bat')

movies.pop('sholay') 

# update
movies['inception'] = 'dream within dream with recursion logic'

# update 2
movies['batman'] += ' and fights crimes at nights'
pprint(movies)