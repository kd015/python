#looping in tuple:
#tuple with one element
#tuple without parathesis
#tuple unpacking
#list inside tuple
#some function that can be use with tuple!!

mixed = (1,2,3,4.0)
for i in mixed:
    print(i)
    
num = (1)
num2 = (1,) #ek hi element ke liye, commas zruri for tuple creation!
print(type(num))
print(type(num2))

#tuple without parathesis
name = 'Krishna', 'Dev', 'Yadav'
print(type(name))

#tuple unpacking
fname, m_name, l_name = name  #jitne variable hai, utne variable lo!!
print(fname)

#list inside tuple
fav = ('Maths', ['PPS','Python','Cyber']) #tuple ke ander agr list hai to: add aur remove kr skte hai!!
fav[1].pop()
print(fav)

#some function that can be use with tuple!!
#min(), max, sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))