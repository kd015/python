name = input("Enter the string: ")
#reverse = name[::-1]
reverse = name[-1::-1]
if ( name == reverse ):
    print("Palindrome String")
    
else:
    print("Not a Palindrome String!!")