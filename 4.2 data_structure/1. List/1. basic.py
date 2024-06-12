#List -- > Ordered collection of items

# num = [ 1, 2, 3 ]
# word = [ "word1", "word2"]
# mix = [ 1, 2, "words", 3.14 ]
# print(num)
# print(word)
# print(mix)
# print(num + word)   #joinning two strings = concatenate 
# print(type(mix))
# print(num[2])
# print(mix[1::])

# mix.append(2.14)  #append last me add krega
# print(mix)

n = int(input("Enter the year : "))
if ( (n % 100 != 0 ) or ( n % 400 == 0 and n % 4 == 0 ) ):
    print("leap year")
else:
    print("Not a leap year!!")