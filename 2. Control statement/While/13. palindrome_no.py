n = int(input("enter the number :"))
temp = n
rev = 0
while ( temp > 0 ):
    i = temp % 10
    rev = rev * 10 + i
    temp = temp // 10
    
if ( n == rev ):
    print("Palindrome No.")
else:
    print("Not a palindrome")