import os

def read(filepath=None):
    if filepath:
        if os.path.exists(filepath):
            with open(filepath,errors='ignore') as f:
                return f.read()
        else:
            print('invalid path')
            return None 
    else:
        print('no filepath given')
        return None