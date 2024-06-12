#LCM of two number!!
# def LCM(n1, n2):
#     i = 1
#     while ( True ): #true ke place pe i<= n2 kr sktehai!!
#         factor = n1 * i
#         if ( factor % n2 == 0):
#             return factor
#         i = i + 1
        
# print(LCM(5,20))

def Least(n1, n2):
    if ( n1 < n2 ):
        return n1
    else:
        return n2
    
def GCD(n1, n2):
    gcd = 1
    i = 2
    least = Least(n1, n2)
    while ( i <= least ):
        if ( n1 % i == 0 and n2 % i == 0):
            gcd = i
        i = i + 1
    return gcd
    
print(GCD(15,30))


