from helper import read

data = read('pride_n_prejudice.txt')

# display the top 100 words that occur in the file
# 0. cleaning
# 1. all words list 
# 2. loop count each word and put ans in dict
# 3. sort the dict with value

def clean(data):
    from string import punctuation
    for p in punctuation+'â€':
        data = data.replace(p,'')
    return data

def word_count(words):
    wordcount = {}
    for w in set(words):
        wordcount[w] = words.count(w)
    return wordcount

words = clean(data).lower().split()
wc = word_count(words)
wc = sorted(wc.items(), key= lambda d: d[-1] )
print(wc[-100:])
