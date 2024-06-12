# def No_Of_Occurrence(l, n):
#     count = 0
#     for i in l:
#         if ( i == n ):
#             count = count + 1
#     return count

# print(No_Of_Occurrence([10,20,40,20,30,40,20,],10))

from array import *
a1 = array('i',[1,2,3,4,5])
print(type(a1))
for x in a1:
    print(x)
    
for y in range(len(a1)):
    print(a1[y], end = " ")