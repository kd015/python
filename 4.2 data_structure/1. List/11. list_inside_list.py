matrix = [[1,2,3],[4,5,6],[7,8,9]]  #2nd list
'''for sublist in matrix:
    for j in sublist:
        print(j)
        
        
print(matrix[1][1])

print(type(matrix))'''

#Generate list with range function
#More about pop method
#Index method
#Pass list to a function!
'''
numbers = list(range(1,11))
print(numbers)

popped_items = numbers.pop()
print(numbers)

print(numbers.index(1))  #agr jyada same wale hai to: index(element_name, start kaha se, stop kaha tk)

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))'''


#Problem: l = [ 1, 2, 3], return [ 1, 4, 9]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def Square_of_number(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

print(Square_of_number(l))