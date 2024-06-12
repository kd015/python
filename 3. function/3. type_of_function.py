#No argument no return
'''def add():
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    c = a + b
    print("Addition = ", c)
    
add()'''

#With argument no return:
'''def add(a, b):
    c = a + b
    print("Addition of these two = ",c)
    
x = int(input("enter the number 1: "))
y = int(input("enter the number 2: "))
add(x,y)'''


#With argument with return
''''def add(a, b):
    c = a + b
    return c
    
x = int(input("enter the number 1: "))
y = int(input("enter the number 2: "))
z = add(x,y)
print("Addition of these two are ",z)'''

#No argument with return:
def add():
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    c = a + b
    return c
    
z = add()
print("Addition = ", z)