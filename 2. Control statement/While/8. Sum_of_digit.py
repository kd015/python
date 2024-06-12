n = int(input("enter the number: "))
sum = 0
while ( n > 0 ):
    sum = sum + n % 10
    n = n // 10
print("Sum of digits = ",sum)




#sum of square of digits:

# n = int(input("enter the number: "))
# sum = 0
# while ( n > 0 ):
#     i  = ( n % 10 )
#     sum = sum + ( i ** 2 )
#     n = n // 10
# print("Sum of square of digits = ",sum)




#sum of cube of digits:

# n = int(input("enter the number: "))
# sum = 0
# while ( n > 0 ):
#     i  = ( n % 10 )
#     sum = sum + ( i ** 3 )
#     n = n // 10
# print("Sum of cube of digits = ",sum)