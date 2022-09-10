# variable arguments - args
# keywords arguments - kwargs

def total(*values):
    t = 0
    for i in values:
        if isinstance(i,(int,float)):
            t +=i
    return t

o = total(1,2,3,4)
print(o)
o = total()
print(o)
o = total(1,2,321,312,312,12,3,13,123,123,12,312,3,123,12)
print(o)
o = total(1,2,321,'a',312,312,'c',12,3,13,123,123,12,312,3,123,12)
print(o)




