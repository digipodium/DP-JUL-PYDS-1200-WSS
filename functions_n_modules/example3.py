data = "" # global variable

def data_appender(s):
    global data # this line tell data_appender that we have a global var data
    if len(s) > 0:
        data += s


# call
data_appender('hello')
data_appender('world')
data_appender('this is a simple function')
data_appender('pehle istemal kre phir vishwas kre')

print(data)