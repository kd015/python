n = int(input("Enter a number :"))
temp = n
sum = 0
while ( temp > 0 ):
    i = temp % 10
    sum = sum + ( i ** 3 )
    temp = temp // 10
if ( sum == n ):
    print("Armstrong")
else:
    print("Not a Armstrong")