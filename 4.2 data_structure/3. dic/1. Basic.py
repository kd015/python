#dictionaries intro:
'''
why we use dictionaries?
because of limitation os list, list is not enough to represent data!

dictionaries is nothing but unordered collection of data in key: value pair!

'''
#how to create dict:

user = {'name':'Krishna','age':19}
user1 = dict(name = 'Krishna',age = 19)
print(user)
print(user1)
print(type(user))

#how to access data:

#through key: get access data:

print(user['name'])
print(user1['age'])

#dict ke andar: numbers, string, list and dict store kr skte hai!

user_info = {
    'name' : 'Krishna',
    'age' : 19,
    'fav_movie' : ['3_I','BALA', 'MAAN', 'DHARKAN'],
    'fav_cricket_player' : ['ROHIT','VIRAT','DHONI'],
}

print(user_info['fav_cricket_player'])

#how to add data ti empty dict:

user_info2 = {}
user_info2['name'] = 'Krishna'
user_info2['age'] = '19'
user_info2['fav_player'] = 'Virat'
print(user_info2)