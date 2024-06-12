name = input("Enter the name :")
vowel_count = 0
conso_count = 0
for i in range(0,len(name)):
    if (name[i] != " "):
        if ( name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] == 'o' or name[i] == 'u' or
         name[i] == 'A' or name[i] == 'E' or name[i] == 'I' or name[i] == 'O' or name[i] == 'U' ):
            vowel_count = vowel_count + 1
        else:
            conso_count = conso_count + 1
        
print("Total vowel = ", vowel_count)
print("Total conso = ", conso_count)