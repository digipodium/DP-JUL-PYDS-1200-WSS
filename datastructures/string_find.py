# find and index are same (similar actually)

msg = 'This is a place to find the answers related to coding.'

print("place:",msg.find('place'))
print("palace:",msg.find('palace')) # -1 means not found

val =  msg.find('answer')
if val == -1:
    print('word not found')
else:
    print(f'word found at {val} index')

print('is:', msg.find('is') )
print('is:', msg.index('is') )

print('is:',msg.find('is',3)) # 3 is the start point for searching

print('to', msg.find('to'))
print('to', msg.rfind('to')) # search from reverse 