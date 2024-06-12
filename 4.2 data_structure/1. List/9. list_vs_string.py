#string and list difference: strings are immutable, lists are mutable

s = "string"  #ek bar declare to fixed
t = s.title()  #new string krta hai
print(s)
print(t)

l = [1, 2, 3]
print(l)
l.pop()
print(l)