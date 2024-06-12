# #max element
# my_list = [12,121,54,34,5]
# max_value = my_list[0]
# for x in my_list:
#     if ( x > max_value ):
#         max_value = x
         
# print(max_value)

# def min_element(l):
#     min_value = l[0]
#     for y in l:
#         if ( y < min_value ):
#             min_value = y
#     return min_value

# print(min_element([34,54,2,3,56,10]))

# s = "I have Mushan"
# pos = 0
# for i in range(len(s)):
#     #if ( s[i] % 2 == 0):
#     print(s[i]," -------> ", pos)
#     pos += 1
    
s = "I have Mushan"
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i]," ------> ", i)
        #print(i)
    
    