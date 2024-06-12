n = int(input("enter the number :"))
rev = 0
while ( n > 0 ): 
    i = n % 10
    rev = rev * 10 + i
    n = n // 10
print("Reversed digit = ",rev)


#Other ways!!

# n = int(input("enter the number :"))
# reverse = str("")
# while ( n > 0 ):
#     i = str(n % 10)
#     reverse = reverse + i
#     n = n // 10
# print("reverse = ",reverse)