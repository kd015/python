n = int(input("eneter the number :"))
product = 1
while ( n > 0 ):
    i = n % 10
    product = product * i
    n = n // 10
print("product of digits = ",product)