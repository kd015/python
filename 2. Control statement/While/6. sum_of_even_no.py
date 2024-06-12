# n = int(input("enter the value of n: "))
# i = 2
# sum = 0
# while ( i <= n ):
#     sum = sum + i
#     print(i)
#     i = i + 2
# print("Sum of even",sum )

n = int(input("enter the value of n: "))
i = 1
sum = 0 
while ( i <= n):
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print("Sum of even no. = ",sum )