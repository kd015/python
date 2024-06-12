user_info = {
    'name' : 'Krishna',
    'age' : 19,
    'fav_movie' : ['3_I','BALA', 'MAAN', 'DHARKAN'],
    'fav_cricket_player' : ['ROHIT','VIRAT','DHONI'],
}

#in keyword: ye bs 'key' ke liye check krta hai!!
'''
if 'name' in user_info:
    print("Present")
    
else:
    print("Not present!!")
    
#values ke liye use: values() #value method
if 'Krishna' in user_info.values():
    print("Present")
    
else:
    print("Not present!!")
    
#looping se to bs keys hi aayega bhai: agr value chahiye to values() method
for i in user_info:
    print(i)
    
for i in user_info.values():
    print(i)
    
user_info_keys = user_info.keys()   #keys method hota jo keys deta hai!!
print(user_info_keys)
print(type(user_info_keys))

#looping in dict:
for i in user_info:
    print(i)
    print(user_info[i])'''
    
#sbse best hai: items() method:  (ye tuple deta hai: 1st element: key aur second element value:)
user_items = user_info.items()
print(user_items)
print(type(user_items))




    
    
