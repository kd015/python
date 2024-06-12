#data ko add krne ke liye: append, extend, insert

#data ko delete krne ke liye: pop, remove, del


'''fruits = [ 'orange', 'apple', 'pear', 'banana', 'kiwi']

fruits.pop()  #last element ko delete kr dega
print(fruits)

fruits.pop(1)  #1 wale index pe jo hai = > delete
print(fruits)'''

#delete operator:
'''fruits = [ 'orange', 'apple', 'pear', 'banana', 'kiwi']

del fruits[0]
print(fruits)'''

#remove method:
fruits = [ 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

'''fruits.remove('banana')  #ws element ko remove kr dega!!
print(fruits)'''

'''fruits.remove('mango')  #x not in list
print(fruits)'''

fruits.remove('apple')  #pahle wale apple ko delete krega!!
print(fruits)