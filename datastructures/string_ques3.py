# wap to remove all the punctuations from the string

from string import punctuation

msg = 'he@#%ll@!()!@(o: &*(@!w#&o!*r(()!@#ld@ '
for p in punctuation:
    msg = msg.replace(p,'')
print(msg)