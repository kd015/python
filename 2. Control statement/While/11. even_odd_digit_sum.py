n = int(input("enter the number :"))
even_sum = 0
odd_Sum = 0
while ( n > 0 ):
    i = n % 10
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_Sum = odd_Sum + i
    n = n // 10
    
print("Even digit sum = ",even_sum)
print("odd digit sum = ",odd_Sum)