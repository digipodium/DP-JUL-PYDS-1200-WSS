# Task. count the occurence of all vowels in a string
# output:
# a - 1
# e - 4
# i - 2
sentence = 'count the occurence of all vowels in a string'
for vowel in 'aeiou':
    print(f"{vowel} counted {sentence.lower().count(vowel)} times")