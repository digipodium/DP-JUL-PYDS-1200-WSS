# nested dict
from pprint import pprint

emps = {
     'chandu': {
        'name': 'chandu sharma',
        'salary':15000,
        'desgination': 'foreman'
     },
     'rohit': {
        'name' : 'rohit kumar singh',
        'salary':19999,
        'designation':'Assistant 2',
        'manager':'ravi prakash'
     },
     'bhanu': {
        'name':'Bhanu pratap',
        'salary': 30000,
        'designation':'system officer',
     }
}

pprint(emps)

print("designation",emps['chandu']['desgination'])

for key,data in emps.items():
    print(key,"⤵️")
    for k,v in data.items():
        print(k, v)
    print('--'*10)