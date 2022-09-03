info_dict ={
    'series' : 'Mistborn', 
    'title' : 'The Final Empire',
    'author' : 'Brandon Sanderson', 
    'publisher' : 'tor.com',
    'price' : 2099, 
    'year' : 2002 
}       

# update existing key
info_dict['price'] = 599
print(info_dict)

# adding a new key value pair
info_dict['rating'] = 10
print(info_dict)
